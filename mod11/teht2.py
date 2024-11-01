class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def tulosta_ominaisuudet(self):
        print(f"Rekkari: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} km/h")
        print(f"Nopeus: {self.nopeus} km/h, Matkamittari: {self.matka} km")

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, aika):
        self.matka += aika * self.nopeus

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_ominaisuudet(self):
        super().tulosta_ominaisuudet()
        print(f"Akkukapasiteetti: {self.akkukapasiteetti} kWh")


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki

    def tulosta_ominaisuudet(self):
        super().tulosta_ominaisuudet()
        print(f"Bensatankin koko: {self.bensatankki} l")

s = Sahkoauto("ABC-15", 180, 52.5)
p = Polttomoottoriauto("ADC-123", 165, 32.3)

s.kiihdyta(120)
p.kiihdyta(150)

s.kulje(3)
p.kulje(3)

s.tulosta_ominaisuudet()
p.tulosta_ominaisuudet()
