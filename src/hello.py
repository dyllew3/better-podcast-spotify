import json
from typing import Any, Union
from flask import Flask, render_template, jsonify
from markupsafe import escape
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyOAuth

from search import PodcastInfo, load_podcast_from_json

app: Flask = Flask(__name__)
app.config['JSON_AS_ASCII'] = True

scope = "user-library-read"
sp = Spotify(auth_manager=SpotifyOAuth())

@app.route("/")
def hello_world() -> str:
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name: str):
    return f"Hello, {escape(name)}!"

@app.route("/search")
def search() -> str:
    return ""

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