from time import sleep
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file("index.html")

PLAYLIST = [
        { "name": "My favorite",
          "band": "This band"
        },
        { "name": "Second favorite",
          "band": "This other band"
        }
    ]

@app.route("/playlist", methods=["GET"])
def getplace():
    sleep(10)
    return json.dumps(PLAYLIST)

@app.route("/add", methods=["POST"])
def addSong():
    
    song = json.loads(request.data)
    sleep(1)
    if song not in PLAYLIST:
        PLAYLIST.append(song)
    return json.dumps(PLAYLIST)

@app.route("/remove", methods=["POST"])
def removeSong():
    song = request.get_json()
    print(song)
    if song in PLAYLIST:
        PLAYLIST.remove(song)
        
    sleep(1)
    return json.dumps(PLAYLIST)

if __name__ == "__main__":
    app.run(debug=True)