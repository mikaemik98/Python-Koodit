import random

class Autotalli:
    def __init__(self):
        self.autot = []

    def auto_sisaan(self, auto):
        if auto not in self.autot:  # Tarkistetaan, ettei auto ole jo tallissa
            self.autot.append(auto)

    def auto_ulos(self, auto):
        self.autot.remove(auto)

    def tulosta_inventaario(self):
        print("Autot tallissa:")
        for auto in self.autot:
            auto.tulosta_ominaisuudet()


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


class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus, osallistujat):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus = pituus
        self.osallistujat = osallistujat

    def tunti_kuluu(self):
        for auto in self.osallistujat:
            nopeuden_muutos = random.randint(-10, 15)  # Arvotaan nopeuden muutos
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)  # Kuljetaan tunti nykyisellä nopeudella

    def tulosta_tilanne(self):
        print(f"\nTilanne kilpailussa '{self.kilpailun_nimi}':")
        print(f"{'Rekkari':<10}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka'}")
        print("-" * 40)
        for auto in self.osallistujat:
            print(f"{auto.rekisteritunnus:<10}{auto.huippunopeus:<15}{auto.nopeus:<10}{auto.matka} km")

    def kilpailu_ohi(self):
        for auto in self.osallistujat:
            if auto.matka >= self.pituus:  # Tarkistetaan, onko joku auto maalissa
                return True
        return False


if __name__ == "__main__":
    # Luodaan autot ja autotalli
    talli = Autotalli()
    for i in range(10):
        rekisteritunnus = f"ABC-{i+1}"
        huippunopeus = random.randint(100, 200)
        uusi_auto = Auto(rekisteritunnus, huippunopeus)
        talli.auto_sisaan(uusi_auto)

    # Luodaan kilpailu
    kilpailu = Kilpailu("Suuri romuralli", 8000, talli.autot)

    # Kilpailun simulointi
    tunti = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunti += 1

        # Tulostetaan tilanne kymmenen tunnin välein
        if tunti % 10 == 0:
            kilpailu.tulosta_tilanne()

    # Lopullinen tilanne, kun kilpailu päättyy
    print("\nKilpailu päättyi! Lopputilanne:")
    kilpailu.tulosta_tilanne()
