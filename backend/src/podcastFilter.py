from typing import Any, Union
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask.wrappers import Response
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyOAuth


app: Flask = Flask(__name__, static_folder="static\\")
app.config['JSON_AS_ASCII'] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

scope = "user-library-read"
sp = Spotify()

@app.route("/")
@app.route("/show/<id>")
@app.route("/episode/<id>")
def home(id: str = "") -> str:
    return app.send_static_file("index.html")

@app.route("/next", methods = ["POST"])
def load_episodes() -> None:
    try:
        if not request.is_json:
            return "Invalid json body given", 400

        body_json: Union[Any, None] = request.get_json()
        return jsonify(sp.next(body_json["episodes"]))
    except Exception as err:
        print(err)
        return "Exception occured when getting next", 500


@app.route("/v1/show/<id>")
def get_show_object(id: str) -> Response:
    try:
        loaded_show: Any | None = sp.show(id)
        if loaded_show == None:
            print(f"Unable to load id: {id}" )
            return Response(status=500)
        else:
            return jsonify(loaded_show)
    except Exception as err:
        print(f"Error occurred {err}")
        return Response(status=500)

@app.route("/v1/episode/<id>")
def get_episode_object(id: str) -> Response:
    try:
        loaded_show: Any | None = sp.episode(id)
        if loaded_show == None:
            print(f"Unable to load episode id: {id}" )
            return Response(status=500)
        else:
            return jsonify(loaded_show)
    except Exception as err:
        print(f"Error occurred {err}")
        return Response(status=500)

@app.route("/search")
def search_for_show() -> Response:
    searchStr: Union[str, None] = request.args.get("name")
    if searchStr == None:
        print("No name given")
        return Response(status=500)
    return jsonify(sp.search(searchStr,10,0,type="show"))