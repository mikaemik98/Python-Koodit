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

    def tunti_kuluu(self):
        for auto in self.Auto:
            nopeuden_muutos = (-10, 15)  # Arvotaan nopeuden muutos
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def kulje(self, aika):
        self.matka += aika * self.nopeus

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_ominaisuudet(self):
        super().tulosta_ominaisuudet()
        print(f"Akkukapasiteetti: {self.akkukapasiteetti}")


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki

    def tulosta_ominaisuudet(self):
        super().tulosta_ominaisuudet()
        print(f"Bensatankin koko: {self.bensatankki}")

s = Sahkoauto("ABC-15", "180km/h", "52.5kWh")
p = Polttomoottoriauto("ADC-123", "165km/h", "32.3l")

s.kiihdyta(120)
p.kiihdyta(150)

s.tulosta_ominaisuudet()
p.tulosta_ominaisuudet()
