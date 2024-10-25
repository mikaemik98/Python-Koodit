import random

class Autotalli:
    def __init__(self):
        self.autot = []

    def auto_sisaan(self, auto):
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


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def tulosta_ominaisuudet(self):
        print(f"Rekkari: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus}")
        print(f"Nopeus: {self.nopeus}, matkamittari: {self.matka}")

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, aika):
        # aika tunneissa
        self.matka += aika * self.nopeus


if __name__ == "__main__":
    talli = Autotalli()
    for i in range(10):
        rekisteritunnus = f"ABC-{i+1}"
        huippunopeus = random.randint(100, 200)
        uusi_auto = Auto(rekisteritunnus, huippunopeus)
        talli.auto_sisaan(uusi_auto)

    kilpailu_kaynnissa = True
    while kilpailu_kaynnissa:
        for auto in talli.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)
            if auto.matka >= 1000:
                kilpailu_kaynnissa = False
                break

    print("Kilpailu päättyi! Lopputilanne: ")
    talli.tulosta_inventaario()
