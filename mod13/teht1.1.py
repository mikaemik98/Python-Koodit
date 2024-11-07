import app
from flask import Flask, Response, render_template
import json
import alkulukulaskuri

@app.route('/alkuluku/<alkuluku>')
def alkuluku(alkuluku):
    try:
        luku = int(alkuluku)
        alkuluku = alkulukulaskuri.laske(luku)

        tilakoodi = 200
        vastaus = {
            "Number": 31,
            "isPrime": alkuluku

        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi
        }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")