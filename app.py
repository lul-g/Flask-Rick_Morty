from flask import Flask, render_template
import urllib.request, json
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def get_movies():
    url = "https://rickandmortyapi.com/api/character"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])