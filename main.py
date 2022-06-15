from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from flask import jsonify
import random
import json


app = Flask(__name__)


@app.route("/asdf")
def home():
    about_link = url_for("home")
    return render_template("index.html", link=about_link)


@app.route('/', methods=["get", "post"]) #formular erstellt bzw. verknüfung, mit get und post wird entgegengenommen und wiedergegeben
def formular():
    if request.method.lower() == "post":
        zutaten = request.form["erste_zutat"]
        return redirect(url_for("zutaten"))
     #   return render_template('formular.html')
   # if request.method.lower() == "post":
    #    name = request.form['vorname']
     #   return(name)
    else:
        return render_template("formular.html")


@app.route("/zutaten", methods=["get", "post"])
def zutaten():
    if request.method.lower() == "post":
        zutaten = request.form["erste_zutat"]
        return render_template("zutaten.html", zutaten=zutaten)
    else:
        return redirect(url_for("error.html"))


@app.route("/error")
def error():
    return render_template("error.html")


def load_daten():
    datei_name = "data.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt


@app.route("/liste")
def auflisten():
    drinks = load_daten()

    return drinks






@app.route("/")
def hello():
    names = ["Sydney", "Silvan", "Furkan", "Gianluca", "Domingo"]
    name_choice = random.choice(names)
    about_link = url_for("about")
    return render_template("index.html", name=name_choice, link=about_link)


@app.route("/menu")
def menu():
    about_link = url_for("menu")
    return render_template("menu.html", link=about_link)


@app.route("/about")
def about():
    return "Bitte gib "


@app.route('/hello/<name2>')
def begruessung(name2):
    return "Hallo " + name2 + "!"




@app.route("/list")       # die im Formular eingegebenen Werte auflisten
def auflistng():
    elemente = ["Money boy", "yolo", "swag", "dreh den swag auf"]
    return render_template("liste.html", html_elemente=elemente)


@app.route("/table")
def tabelle():

    biere = [
        {
            "name": "Panix Perle",
            "herkunft": "Glarus",
            "vol": "4.6",
            "brauerei": "Adler",
            "preis": 2.40
        },
        {
            "name": "Retro",
            "herkunft": "Luzern",
            "vol": "4.9",
            "brauerei": "Eichhof",
            "preis" : 1.80
        },
        {
            "name": "Quöllfrisch",
            "herkunft": "Appenzell",
            "vol": "4.8",
            "brauerei": "Locher",
            "preis" : 2.50
        }
    ]
    for bier in biere:
        preis = bier["preis"]
        tax = berechnen(preis)
        bier["steuern"] = tax



    table_header = ["Name", "Herkunft", "Vol%", "Brauerei", "Preis", "Steuern"]
    return render_template("beer.html", beers=biere, header=table_header)


@app.route("/abgaben")
def yo(preis):
    abgaben_betrag = abgaben(preis)
    return render_template("preis.html", abgabe=abgaben_betrag)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
