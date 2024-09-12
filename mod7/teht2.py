def kysy_nimet():
    nimet = set()
    nimi = input("Syötä nimi tai paina enter lopettaaksesi ohjelma: ")

    while nimi != "":
        if nimi in nimet:
            print("Aijemmin syötetty nimi")
        else:
            print("Uusi nimi")
            nimet.add(nimi)

        nimi = input("Syötä nimi tai paina enter lopettaaksesi ohjelma: ")

    return nimet

def tulosta_nimet(nimet):
    print("Syötetyt nimet: ")
    for nimi in nimet:
        print(nimi)

syötetyt_nimet = kysy_nimet()
tulosta_nimet(syötetyt_nimet)
