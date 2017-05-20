from flask import Flask
from flask import jsonify
from flask import render_template
from api.steam import Steam
import os

template_dir = os.path.abspath('api/views')

app = Flask(__name__, template_folder=template_dir)


@app.route("/get")
def get():
    games = Steam().get_games_statistics()
    return jsonify(games)


@app.route("/get_template")
def get_template():

    games = Steam().get_games_statistics()

    return render_template('index.html', games=games)

if __name__ == "__main__":
    app.run()