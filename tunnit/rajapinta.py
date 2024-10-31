import requests

def search_show(search_term):
    # HTTP GET https://api.tvmaze.com/search/shows?q=girls
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"
    # käsitellään mahdolliset virheet verkkoyhteydessä
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

    if len(response_body) < 1:
        print("Ei tuloksia")
        return
    # Näytetään vain ensimmäinen hakutuloksen nimi
    #print(response_body[0]['show']['name'])

    # iteroidaan response body (http-vastauksen runko) silmukalla
    print("Kaikki hakutulokset\n--------------")
    for item in response_body:
        print(item['show']['name'])
        print(f"TV-ohjelman tyyppi: {item['show']['type']}")
        for genre in item['show']['genres']:
            print(genre)
        print("---")

#search_show("Girls")
search_show(input("Anna TV-hakusana: "))