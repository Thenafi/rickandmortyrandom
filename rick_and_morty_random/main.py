from flask import Flask, redirect
import random

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return " Visit <a href='https://github.com/Thenafi/rickandmortyrandom'>Github</a> for usage"


@app.route("/random_character")
def random_character():
    print(random.randint(3, 9))
    return redirect(
        f"https://rickandmortyapi.com/api/character/{random.randint(0, 826)}"
    )


@app.route("/random_image")
def random_image():
    print(random.randint(3, 9))
    return redirect(
        f"https://rickandmortyapi.com/api/character/avatar/{random.randint(0, 826)}.jpeg"
    )
