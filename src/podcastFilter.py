from typing import Any, Union
from flask import Flask, render_template, request, jsonify
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyOAuth
from episode import Episode, load_episode_from_json

from podcast import PodcastInfo, load_podcast_from_json

app: Flask = Flask(__name__, static_folder="static\\")
app.config['JSON_AS_ASCII'] = True

scope = "user-library-read"
sp = Spotify()

@app.route("/")
def home() -> str:
    return render_template("home.html")

@app.route("/search")
def search() -> str:
    return ""

@app.route("/next", methods = ["POST"])
def load_episodes() -> None:
    try:
        if request.is_json:
            return "Invalid json body given", 400

        body_json: Union[Any, None] = request.get_json()
        
        return jsonify(sp.next(body_json))
    except Exception as err:
        print(err)
        return "Exception occured when getting next", 500

@app.route("/show/<id>")
def get_show_id(id: str) -> Union[str, None]:
    loaded_show: Any | None = sp.show(id)
    if loaded_show == None:
        return "Unable to load show"
    else:
        podcast: Union[PodcastInfo, None] = load_podcast_from_json(loaded_show)
        if podcast == None:
            return "Error loading from json string."
        else:
            return render_template("show.html", podcast=podcast)

@app.route("/episode/<id>")
def get_episode_id(id: str) -> Union[str, None]:
    loaded_episode: Any | None = sp.episode(id)
    if loaded_episode == None:
        return "Unable to load episode"
    else:
        episode: Union[Episode, None] = load_episode_from_json(loaded_episode)
        if episode == None:
            return "Error loading from json string."
        else:
            return render_template("episode.html", episode=episode)