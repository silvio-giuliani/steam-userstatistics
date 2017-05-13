from flask import Flask
from flask import jsonify
from api import steam


app = Flask(__name__)


@app.route("/get")
def get():
    games = steam.Steam().get_games_statistics()
    return jsonify(games)

if __name__ == "__main__":
    app.run()