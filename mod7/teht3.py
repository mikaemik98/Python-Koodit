def kysy_lentoasema():
    icao = {'EFHK': 'Helsinki-Vantaa', 'CYOH': 'Oxford House lenoasema', 'EFHV': 'Hyvinkään lentoasema'}

    valinta = ""

    while valinta != "3":
        valinta = input("Valitse toiminto: [1] Syötä uusi lentoasema, [2] Hae lentoasema, [3] Lopeta: ")
        if valinta == "1":
            icao_koodi = input("Syötä lentoaseman icao-koodi: ")
            if icao_koodi in icao:
                print("Lento asema on jo olemassa.")
            else:
                nimi = input("Syötä lentoaseman nimi: ")
                icao[icao_koodi] = nimi
                print(f"Lentoasema {icao_koodi} - {nimi} lisätty.")

        elif valinta == "2":
            icao_koodi = input("Syötä haettavan lentoaseman icao-koodi: ")
            if icao_koodi in icao:
                print(f"{icao_koodi}: {icao[icao_koodi]}")
            else:
                print("Lentoasemaa ei löytynyt.")

        elif valinta != "3":
            print("Virheellinen valinta, yritä uudelleen.")
    print("Ohjelma lopetettu.")

kysy_lentoasema()