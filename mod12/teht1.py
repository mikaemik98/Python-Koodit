import requests

def hae_chuck_norris_vitsi():
    url = f"https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Verkkovirhe!")
        # print(e)
        return

    # testataan, että http status koodi OK
    if response.status_code != 200:
        print(f"HTTP-yhteysvirhe {response.status_code}")
        return

    response_body = response.json()

    print(response_body['value'])

hae_chuck_norris_vitsi()