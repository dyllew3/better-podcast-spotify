import json
import os
import spotipy
import uuid

from datetime import timedelta
from flask import Flask, request, redirect, session, jsonify
from flask_cors import CORS
from flask_session import Session
from flask.wrappers import Response
from models import Podcast
from redis import Redis
from spotipy.client import Spotify
from typing import Any, Union

redis_inst = Redis(host='localhost', port=6379, db=0)

app: Flask = Flask(__name__, static_folder="static\\")
app.config['JSON_AS_ASCII'] = True

# Setup session
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)

# Setup cross origin requestd
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

scope = "user-library-read"

# Create spotify cache folder
caches_folder = './.spotify_caches/'
if not os.path.exists(caches_folder):
    os.makedirs(caches_folder)

def session_cache_path() -> str:
    """Path to the session cache."""
    if not session.get("uuid"):
        # Step 1. Visitor is unknown, give random ID
        session["uuid"] = str(uuid.uuid4())
    return caches_folder + session.get('uuid')


def get_spotify_object() -> Spotify:
    """ Get spotify object to perform spotify API requests.
    """
    cache_handler = spotipy.cache_handler.CacheFileHandler(cache_path=session_cache_path())
    auth_manager = spotipy.oauth2.SpotifyOAuth(
        cache_handler=cache_handler, 
        show_dialog=True,
        client_id=os.environ['client_id'],
        client_secret=os.environ['client_secret'],
        scope=scope,
        redirect_uri=os.environ['redirect_uri'])
    return spotipy.Spotify(auth_manager=auth_manager)


@app.route("/")
@app.route("/show/<id>")
@app.route("/episode/<id>")
def home(id: str = "") -> str:
    """Home page route"""
    # Step 1. Visitor is unknown, give random ID
    if not session.get("uuid"):
        session["uuid"] = str(uuid.uuid4())
    
    cache_handler = spotipy.cache_handler.CacheFileHandler(cache_path=session_cache_path())
    auth_manager = spotipy.oauth2.SpotifyOAuth(
        cache_handler=cache_handler, 
        show_dialog=True,
        client_id=os.environ['client_id'],
        client_secret=os.environ['client_secret'],
        scope=scope,
        redirect_uri=os.environ['redirect_uri'])

    # Check for access token in request and add it to auth
    if request.args.get("code"):
        auth_manager.get_access_token(request.args.get("code"))
        return redirect('/')

    return app.send_static_file("index.html")


@app.route("/next", methods = ["POST"])
def load_episodes() -> Response:
    """Load the next set of episode for a show if there are more to load"""
    try:
        if not request.is_json:
            return "Invalid json body given", 400

        body_json: Union[Any, None] = request.get_json()
        podcast = Podcast.load_from_json(body_json)

        # If no next just return current podcast
        if not podcast.episodes["next"]:
            return jsonify(podcast.__dict__)

        # Load from cache
        pod_next_key: str = podcast.episodes["next"]
        cache_inst = redis_inst.get(pod_next_key)
        if cache_inst and cache_inst != b'{}':
            print("cache hit")
            return jsonify(json.loads(cache_inst))

        # get next set of episodes if there are more to load
        if podcast.episodes["total"] != len(podcast.episodes["items"]):
            sp = get_spotify_object()
            next_episodes = sp.next(podcast.episodes)
            podcast.merge_episodes(next_episodes)

        # Cache result
        redis_inst.set(pod_next_key, json.dumps(podcast.__dict__), ex=timedelta(days=0.5))
        redis_inst.set(f"podcast_{podcast.id}", json.dumps(podcast.__dict__), ex=timedelta(days=0.5))
        return jsonify(podcast.__dict__)
    except Exception as err:
        print(err)
        return "Exception occured when getting next", 500

@app.route("/v1/show/<id>")
def get_show_object(id: str) -> Response:
    try:
        pod_key: str = f"podcast_{id}"
        cache_inst = redis_inst.get(pod_key)

        if cache_inst and cache_inst != b'{}':
            return jsonify(json.loads(cache_inst))

        sp = get_spotify_object()
        loaded_show: Any | None = sp.show(id)
        podcast: Podcast = Podcast.load_from_json(loaded_show)
        if loaded_show == None:
            print(f"Unable to load id: {id}" )
            return Response(status=500)
        else:
            return jsonify(podcast.__dict__)
    except Exception as err:
        print(f"Error occurred {err}")
        return Response(status=500)

@app.route("/v1/episode/<id>")
def get_episode_object(id: str) -> Response:
    try:
        # Load episode from redis cache
        episode_key: str = f"episode_{id}"
        cache_inst = redis_inst.get(episode_key)
        if cache_inst and cache_inst != b'{}':
            return jsonify(json.loads(cache_inst))

        sp = get_spotify_object()
        loaded_episode: Any | None = sp.episode(id)
        if loaded_episode == None:
            print(f"Unable to load episode id: {id}" )
            return Response(status=500)
        else:
            redis_inst.set(episode_key, json.dumps(loaded_episode), ex=timedelta(days=1))
            return jsonify(loaded_episode)
    except Exception as err:
        print(f"Error occurred {err}")
        return Response(status=500)

@app.route("/search")
def search_for_show() -> Response:
    searchStr: Union[str, None] = request.args.get("name")
    if searchStr == None:
        print("No name given")
        return Response(status=500)
    sp = get_spotify_object()
    result = sp.search(searchStr,10,0,type="show")
    return jsonify(result)