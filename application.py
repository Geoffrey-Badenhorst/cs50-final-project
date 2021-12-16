from pytrends.request import TrendReq
from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp

from helpers import create_trends, find_winner, get_trends


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set language and timezone for pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Global variables
score = 0


@app.route("/game", methods=["GET", "POST"])
def game():
    """Pick correct highest search trend"""

    # Variables
    trends = create_trends()
    trend1 = trends[0]
    trend2 = trends[1]

    global score

    if request.method == "POST":
        winner = find_winner(trend1, trend2)
        score_value = 0
        game_duration = 5

        option1 = [request.form.get("trend1"), trend1]
        option2 = [request.form.get("trend2"), trend2]

        # Conditions for how the game should react when an option is clicked based on how the game is going
        if option1[1] == winner and score < game_duration:
            score += 1
            return render_template("/game.html", trend1 = trend1, trend2 = trend2, score = score, duration = game_duration)
        elif option1[1] == winner and score == game_duration:
            score = 0
            return render_template("/win.html", trends = get_trends())
        elif option1[1] != winner:
            score_value = score
            score = 0
            return render_template("/lose.html", score = score_value)
        elif option2[1] == winner and score < game_duration:
            score += 1
            return render_template("/game.html", trend1 = trend1, trend2 = trend2, score = score, duration = game_duration)
        elif option2[1] == winner and score == game_duration:
            return render_template("/win.html", trends = trend_list)
        elif option2[1] != winner:
            score_value = score
            score = 0
            return render_template("/lose.html", score = score_value)

    elif request.method == "GET":
        return render_template("/game.html", trend1 = trend1, trend2 = trend2, score = 0, duration = 5)


@app.route("/")
def index():
    """Display home page"""

    return render_template("/index.html")


@app.route("/lose")
def lose():
    """Display lose screen"""

    return render_template("/lose.html", score = 0)


@app.route("/rules")
def rules():
    """Display rules page"""

    return render_template("/rules.html")


@app.route("/win")
def win():
    """Display win screen"""

    trends = get_trends()

    return render_template("/win.html", trends = trends)