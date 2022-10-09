from flask import Flask, redirect
import random

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return " Visit <a href='https://github.com/Thenafi/rickandmortyrandom'>Github</a> for usage"


@app.route("/random_character", methods=["GET"])
def random_character():
    return redirect(
        f"https://rickandmortyapi.com/api/character/{random.randint(0, 826)}", 302
    )


@app.route("/random_image", methods=["GET"])
def random_image():
    return redirect(
        f"https://rickandmortyapi.com/api/character/avatar/{random.randint(0, 826)}.jpeg",
        302,
    )
