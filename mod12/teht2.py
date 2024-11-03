import requests

def hae_saa(paikkakunta):
    api_key = "feb915a6854fa3e1891645c6966d2ca6"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print("Verkkovirhe tai ongelma pyynnössä!")
        return

    data = response.json()

    if data.get("cod") != 200:
        print("Paikkakuntaa ei löytynyt!")
        return

    saatilanne = data["weather"][0]["description"]
    lampotila_kelvin = data["main"]["temp"]

    lampotila_celsius = lampotila_kelvin - 273.15

    print(f"Sää {paikkakunta}-paikkakunnalla: {saatilanne}")
    print(f"Lämpötila: {lampotila_celsius:.2f} C")

paikkakunta = input("Syötä paikkakunnan nimi: ")
hae_saa(paikkakunta)
