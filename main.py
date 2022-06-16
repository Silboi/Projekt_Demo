from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from flask import json
import random
import json


app = Flask(__name__)


@app.route("/asdf")
def home():
    about_link = url_for("home")
    return render_template("index.html", link=about_link)


@app.route('/', methods=["get", "post"]) #formular erstellt bzw. verknüpfung, mit get und post wird entgegengenommen und wiedergegeben
def formular():
    if request.method.lower() == "post":
        zutaten = request.form["erste_zutat"]
        return redirect(url_for("zutaten"))
    else:
        return render_template("formular.html")


@app.route("/zutaten", methods=["get", "post"])
def zutaten():
    if request.method.lower() == "post":
        zutaten_1 = request.form["erste_zutat"]
        zutaten_2 = request.form["zweite_zutat"]
        zutaten_3 = request.form["dritte_zutat"]
        return render_template("zutaten.html", zutaten1=zutaten_1, zutaten2=zutaten_2, zutaten3=zutaten_3)

    else:
        about_link = url_for("error")
        return render_template("error.html", link=about_link)


@app.route("/error")
def error():
    return render_template("error.html")


#def load_daten():       # Daten von der json Datei werden geladen
 #   datei_name = "data.json"

  #  try:
   #     with open(datei_name) as open_file:
    #        datei_inhalt = json.load(open_file)
   # except FileNotFoundError:
    #    datei_inhalt = {}

  #  return datei_inhalt


def dictionary_aus_json():          # Daten von der json Datei werden geladen
    with open("data.json") as file:
        data = json.load(file)
    return data


@app.route("/liste")        # Daten werden ausgegeben
def auflisten():
    drinks = dictionary_aus_json()

    return drinks


@app.route("/einkaufszettel")
def rechnen():
    if zutaten1 in data
        return render_template("einkaufsliste.html")

    else:
        about_link = url_for("error")
        return render_template("error.html", link=about_link)










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
