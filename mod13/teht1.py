from flask import Flask, Response, render_template
import json
import alkulukulaskuri

app = Flask(__name__)

@app.route('/alkuluku/<number>')
def alkuluku(number):
    try:
        luku = int(number)
        alkuluku = alkulukulaskuri.laske(luku)

        tilakoodi = 200
        vastaus = {
            "Number": luku,
            "isPrime": alkuluku

        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi
        }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
