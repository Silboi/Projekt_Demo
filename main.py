from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from flask import json
import json
                                            #alles importiert, was benötigt wird

app = Flask(__name__)


#@app.route("/asdf")
#def home():
 #   about_link = url_for("home")
  #  return render_template("index.html", link=about_link)


@app.route('/', methods=["get", "post"]) #formular erstellt bzw. verknüpfung, mit get und post wird entgegengenommen und wiedergegeben
def formular():
    if request.method.lower() == "post":
        zutaten = request.form["erste_zutat"]
        return redirect(url_for("zutaten"))
    else:
        return render_template("formular.html")


@app.route("/zutaten", methods=["get", "post"])
def zutaten():
    zutaten_1 = ""
  #  zutaten_2 = ""
   # zutaten_3 = ""
    drinks_match = []
    karte = {}
    gesamtpreis = 0

    if request.method.lower() == "post":
        zutaten_1 = request.form["erste_zutat".lower()]
   #     zutaten_2 = request.form["zweite_zutat"]
    #    zutaten_3 = request.form["dritte_zutat"]

    karte = dictionary_aus_json()
    drinks_match = []

    for key, value in karte.items():
        for key2, value2 in value.items():
            for key3, value3 in value2.items():
                if key3 == zutaten_1:
                    drinks_match.append([key, 0])

    for key, value in karte.items():
        for element in drinks_match:
            if key == element[0]:
                for key2, value2 in value.items():
                    for key3, value3 in value2.items():
                        gesamtpreis = gesamtpreis + value3["Preis"]
                        element[1] = gesamtpreis

    gesamtpreis = 0

    if len(drinks_match) < 1:                                                   #wenn die Eingabe ungültig ist, dann gibt es das aus
        drinks_match.append(["Diese Zutat ist in keinem Drink vorhanden", ""])          #mit dem Platzhalter, weil es 2 braucht und es unsichtbar ist, wenn es leer ist

    return render_template("zutaten.html", zutaten1=zutaten_1, drinks_match=drinks_match, karte=karte)


def dictionary_aus_json():          # Daten von der json Datei werden geladen
    with open("data.json") as file:
        data = json.load(file)
    return data


@app.route("/liste")        # Daten werden ausgegeben
def auflisten():
    drinks = dictionary_aus_json()

    return render_template("liste.html", drinks=drinks)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
