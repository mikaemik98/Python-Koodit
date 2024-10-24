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


if __name__ == "__main__":
    auto1 = Auto("ABC-123", "142 km/h")

    print("Alkuperäinen nopeus:", auto1.nopeus)

    # Kiihdytykset
    auto1.kiihdytä(30)
    print("Nopeus +30 km/h:", auto1.nopeus)

    auto1.kiihdytä(70)
    print("Nopeus +70 km/h:", auto1.nopeus)

    auto1.kiihdytä(50)
    print("Nopeus +50 km/h:", auto1.nopeus)

    # Hätäjarrutus
    auto1.kiihdytä(-200)
    print("Nopeus hätäjarrutuksen jälkeen:", auto1.nopeus)