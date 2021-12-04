# better-podcast-spotify

Allows for better searching of podcasts on Spotify

## Overview

This allows for more effective filtering of podcasts on spotify. When you go to a podcast page on spotify
it does not allow for searching for specific episodes. So this service allows for finding a podcast
going to its page then filtering the episodes down with a search string.
This search method just checks if the podcast episode name or description contain the string.

Was built using python flask and using vue typescript.
Code is broken down based on Frontend UI and backend code,

## Setup

### Backend

Python >3.7 will be required for download <https://www.python.org/downloads/> .
Then run 'pip install -r requirments.txt' on the requirements.txt in backend\ folder

## Frontend

Node js needs to be installed <https://nodejs.org/en/>
Yarn will need to be installed <https://yarnpkg.com/getting-started/install>
Then go to frontend folder and set the version to latest stable version.
Run 'yarn install' in the folder which the package.json is in.
All typescript code for vue is located in the src/ folder

## Running

First you will need environmental variables set:

+ client_id: The client id of the spotify app
+ client_secret: The client secret of the spotify app
+ redirect_uri: Spotify app redirect uri
+ FLASK_APP: Name of the flask app should match filename i.e 'podcastFilter' for podcastFilter.py
+ NODE_ENV: Set to 'production' when deploying to flask

Then go to frontend folder and run yarn build in the directory with package.json .
This will output the frontend code into the backend\src\static.
Then when trying to deploy the server go to backend\src and run the command 'flask run' this
should launch the server on <http://127.0.0.1:5000>

## API

+ '/v1/show/{id: string}'
+ '/v1/episode/{id: string}'
+ '/search' , Methods = [ GET ], QueryParams = [ name: string  ]
+ '/next', Methods = [ POST ], body: json
+ '/', Methods = [ GET ]
+ '/show/{id: string}', Methods = [ GET ]
+ '/episode/{id: string}', Methods = [ GET ]
