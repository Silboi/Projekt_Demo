from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from flask import json
import json
                                            #alles importiert, was benötigt wird

app = Flask(__name__)


@app.route('/', methods=["get", "post"])            #formular erstellt bzw. verknüpfung, mit get und post wird entgegengenommen und wiedergegeben
def formular():
    if request.method.lower() == "post":
        zutaten = request.form["erste_zutat"]
        return redirect(url_for("zutaten"))         #zu dieser Seite leiten
    else:
        return render_template("formular.html")


@app.route("/zutaten", methods=["get", "post"])
def zutaten():
    zutaten_1 = ""                          #Variable erstellt, zuerst leer
    gesamtpreis = 0                         #Preis definiert, zuerst auf 0

    if request.method.lower() == "post":
        zutaten_1 = request.form["erste_zutat"]

    karte = dictionary_aus_json()           #Daten von json in Variable gespeichert
    drinks_match = []                       #Leerer Dictionary, um diesen später zu füllen

    for key, value in karte.items():                #Loop, um auf die nächste Ebene zu gelangen im Dictionary
        for key2, value2 in value.items():          #Loop, um auf die nächste Ebene zu gelangen im Dictionary, neuer key und value name
            for key3, value3 in value2.items():     #Loop, um auf die nächste Ebene zu gelangen im Dictionary, neuer key und value name
                if key3 == zutaten_1:               #Abfrage, ob eine Zutat übereinstimmt mit den Daten
                    drinks_match.append([key, 0])   #Drinkname (oberste Ebene im Dictionary) in Liste laden für die Ausgabe

    for key, value in karte.items():                                    #Loop, um auf die nächste Ebene zu gelangen im Dictionary
        for element in drinks_match:                                    #Loop für Abfrage
            if key == element[0]:                                       #Vergleich ob Drinkname übereinstimmt mit Abfrage
                for key2, value2 in value.items():                      #Loop, um auf die nächste Ebene zu gelangen im Dictionary, neuer key und value name
                    for key3, value3 in value2.items():                 #Loop, um auf die nächste Ebene zu gelangen im Dictionary, neuer key und value name
                        gesamtpreis = gesamtpreis + value3["Preis"]     #Preis definieren und dazurechnen
                        element[1] = gesamtpreis                        #Speicherung

    gesamtpreis = 0                             #wieder auf 0 setzen

    if len(drinks_match) < 1:                                                   #wenn die Eingabe ungültig ist, dann gibt es das aus
        drinks_match.append(["Diese Zutat ist in keinem Drink vorhanden", ""])          #mit dem Platzhalter, weil es 2 braucht und es unsichtbar ist, wenn es leer ist

    return render_template("zutaten.html", zutaten1=zutaten_1, drinks_match=drinks_match, karte=karte)


def dictionary_aus_json():              # Daten von der json Datei werden geladen
    with open("data.json") as file:
        data = json.load(file)
    return data


@app.route("/liste")             # Daten werden ausgegeben
def auflisten():
    drinks = dictionary_aus_json()              #Speicherung von den Daten

    return render_template("liste.html", drinks=drinks)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
