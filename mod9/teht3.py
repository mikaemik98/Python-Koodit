class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus > int(self.huippunopeus.split()[0]):  # Ota huomioon vain numero
            self.nopeus = int(self.huippunopeus.split()[0])
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, aika):
        # aika tunneissa
        self.matka += aika * self.nopeus


if __name__ == "__main__":
    auto1 = Auto("ABC-123", "142 km/h")

    auto1.matka = 2000
    print(f"Alkuperäinen matka: {auto1.matka}km")

    # Aseta nopeus kutsumalla kiihdytä-metodia
    auto1.kiihdytä(60)
    print("Nopeus asetettu 60 km/h:", auto1.nopeus)

    # Kutsu kulje-metodia 1,5 tunnin ajalle
    auto1.kulje(1.5)
    print(f"Kuljettu matka 1.5 tunnin jälkeen: {auto1.matka}km")