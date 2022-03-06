from crypt import methods
from unittest import result
from boggle import Boggle
from flask import Flask, request, render_template, jsonify, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

boggle_game = Boggle()

@app.route("/")
def boggle_homepage():
    """Displays the Boggle Board on the Homepage"""
    board = boggle_game.make_board()
    session["board"] = board
    high_score = session.get("high_score", 0)
    plays = session.get("plays", 0)
    return render_template("index.html", board=board, high_score=high_score, plays=plays)

@app.route("/check-word")
def check_word():
    """Checks if the Word is in the Game Dictionary"""
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)
    return jsonify({"result":response})

@app.route("/post-score", methods=["POST"])
def post_score():
    """Updates the Score and Number of Plays"""
    score = request.json["score"]
    high_score = session.get("high_score", 0)
    plays = session.get("plays", 0)
    session['plays'] = plays + 1
    session['high_score'] = max(score, high_score)
    return jsonify(brokeRecord = score > high_score)