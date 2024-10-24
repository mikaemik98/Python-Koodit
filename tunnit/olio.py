'''
# Luokka on "ohje" olion luomiselle

class Koira:
    pass

# Olio on luokan ilmentymä
# Pääohjelmasta voi luoda useita olioita

# Luodaan koira-olio
ullan_koira = Koira()
elviiran_koira = Koira()

# Annetaan olioille ominaisuuksia
# Oliokohtaisia

ullan_koira.nimi = "Lissu"
ullan_koira.syntymävuosi = 2015

elviiran_koira.nimi = "Reko"
elviiran_koira.syntymävuosi = 2016
elviiran_koira.karva = "lyhyt"

print(elviiran_koira)
print(f"Ullan koiran nimi on: {ullan_koira.nimi} ja syntymävuosi on: {ullan_koira.syntymävuosi}")

# edellisessä esimerkissä tehtiin luokka ilman ominausuuksia ja metodeja
# olion ominaisuudet annettiin yksi kerrallaan
# Tämä on työlästä ja oikea tapa onkin määritellä ja alustaa ominaisuudet luokan avulla

'''
#Luokkien perusrakenne
'''

class LuokanNimi:

    # __init__ on funktio, erityinen sellainen, kutsutaan konstruktoriksi
    # tätä funktiota kutsutaan aina automaattisesti kun luodaan luokasta olio/instanssi
    # alustajan loppuun EI kirjoiteta return-lausetta
    def __init__(self, parametri1, parametri2):
        self.atribuutti1 = parametri1
        self.atribuutti2 = parametri2

    # metodi
    def metodi(self):
        return

    def metodi2(self):
        return
'''

'''
Laajennetaan yllä olevaa Koira-esimerkkia niin että se alustaa koirien ominaisuudet
'''

class Koira2:
    tehty = 0
    # haukahdus oletusarvo mikäli sitä ei määritetä
    def __init__(self, nimi, syntymävuosi, väri, koko, haukahdus="WOFF"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.väri = väri
        self.koko = koko
        self.haukahdus = haukahdus
        Koira2.tehty = Koira2.tehty + 1

    def printtaa_tiedot(self):
        print(f"Koiran nimi on {self.nimi} ja syntymävuosi on {self.syntymävuosi}")
        return

    def hauku(self, kerrat):
        print(f"Koiran nimi on {self.nimi} joka haukkuu {kerrat} kertaa")
        for i in range(kerrat):
            print(self.haukahdus)
        return



k1 = Koira2("Lissu", 2015, "harmaa", "iso", "WOOF WOOOFF")
k2 = Koira2("Reko", 2016, "ruskea", "pieni", "YIP YIP")
# tämän olion luonnista puuttuu haukahdus attribuutti, joten käyttää oletus
k3 = Koira2("Otto", 2010, "musta", "pieni")
print(f"Koiria on nyt {Koira2.tehty}")

k1.hauku(5)
k2.hauku(10)
k3.hauku(3)

print(k1.nimi, k1.väri, k1.koko)
print(k2.väri)

'''
Laajennetaan yllä olevaa ohjelmaa ja tehdään sinne metodi jossa printataan koirien tiedot
'''

k1.printtaa_tiedot()
k2.printtaa_tiedot()
k3.printtaa_tiedot()

