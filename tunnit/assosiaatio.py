import random

class Autotalli:
    def __init__(self):
        self.autot = []
    def auto_sisaan(self, auto):
        # tarkistetaan, ettei auto ole jo tallissa
        # parempi tapa olisi muuttaa lista joukoksi, jolloin duplikaatteja ei sallita
        for a in self.autot:
            if a == auto: # => True jos viittaavat samaan olioon
                return
        self.autot.append(auto)

    def auto_ulos(self, auto):
        self.autot.remove(auto)

    def tulosta_inventaario(self):
        print("Autot tallissa: ")
        for auto in self.autot:
            auto.tulosta_ominaisuudet()

class Kuljettaja:
    def __init__(self, nimi, ika, auto):
        self.nimi = nimi
        self.ika = ika
        self.auto = auto

    def aja(self):
        print(f"Olen {self.nimi}, {self.ika} ja ajan autoa {self.auto.rek_nro}")
        self.auto.kiihdyta(40)
        self.auto.kulje(1)
        print(self.auto.nopeus)
        self.auto.kiihdyta(140)
        self.auto.kulje(0.1)
        print(self.auto.nopeus)
        self.auto.kiihdyta(-250)
        self.auto.tulosta_ominaisuudet()

class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.nopeus = 0
        self.matka = 0
        self.huippunopeus = huippunopeus
        self.kuljettaja = "Räikkönen"
        print(f"Auto luotu {rek_nro}, huiput: {huippunopeus}")

    def tulosta_ominaisuudet(self):
        print(f"Rekkari: {self.rek_nro}, Huippunopeus: {self.huippunopeus}")
        print(f"Nopeus: {self.nopeus}, matkamittari: {self.matka}")

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        # rajoitetaan kiihdytyksen tulos huippunopeuteen
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        # auto pysähtyy, jos nopeus alle 0
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        # aika tunneissa
        self.matka += aika * self.nopeus

# luodaan oliot ja sijoitetaan viittauksen niihin muuttujiin
a1 = Auto("ABC-123", 120)
a2 = Auto("ZYX-789", 250)
kuski = Kuljettaja("Räikkönen", 40, a1)
kuski.aja()
# vaihdetaan kuljettajan autoa ja ajetaan uudestaan
kuski.auto = a2
kuski.aja()

print("-----------------------------------------------")

# luodaan Autotalli-tyyppinen olio ja sijoitetaan autot sinne

talli = Autotalli()
talli.auto_sisaan(a1)
talli.tulosta_inventaario()
talli.auto_sisaan(a2)
talli.tulosta_inventaario()
#talli.auto_ulos(a1)
talli.tulosta_inventaario()

# Luodaan 10 erilaista auto-oliota autotalliin
for i in range(10):
    uusi_auto = Auto(f"ABC-{i+1}", random.randint(100, 200))
    talli.auto_sisaan(uusi_auto)
    talli.tulosta_inventaario()

"""
a2.kiihdyta(30)
a2.kiihdyta(300)
a1.kiihdyta(-54)
a1.tulosta_ominaisuudet()
a2.tulosta_ominaisuudet()
a2.kiihdyta(-100)
a2.tulosta_ominaisuudet()
#print(f"Rekkari: {a1.rek_nro}, Huippunopeus: {a1.huippunopeus}")
#print(f"Rekkari: {a2.rek_nro}, Huippunopeus: {a2.huippunopeus}")
"""