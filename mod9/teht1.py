class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

auto1 = Auto("ABC-123", "142km/h")
print("Rekisteritunnus: ",auto1.rekisteritunnus)
print("Huippunopeus: ",auto1.huippunopeus)
print("Tämänhetkinen nopeus: ",auto1.nopeus)
print("Kuljettu matka: ",auto1.matka)