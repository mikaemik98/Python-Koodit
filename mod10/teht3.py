class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        # nykyinen kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros < self.alin or kohdekerros > self.ylin:
            return
            # olion omia metodeita kutsuttuaessa käytetään self.
        while kohdekerros > self.kerros:
            self.kerros_ylos()
        while kohdekerros < self.kerros:
            self.kerros_alas()

    def kerros_ylos(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Hissi on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.kerros}")

class Talo:
    def __init__(self, ylin_kerros, alin_kerros, hissi_maara):
        self.kerros_a = alin_kerros
        self.kerros_y = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissi_maara)]

    def aja_hissia(self, hissi_numero, kohdekerros):
        if 0 <= hissi_numero < len (self.hissit):
            print(f"Ajetaan hissiä numero {hissi_numero} kerrokseen {kohdekerros}")
            self.hissit[hissi_numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Virheellinen hissinumero!")

    def palohalytys(self):
        print("Palohälytys, kaikki hissit siirtyvät pohjakerrokseen.")
        for index, hissit in enumerate(self.hissit):
            print(f"Siiretään hissi {index} pohjakerrokseen")
            hissit.siirry_kerrokseen(self.kerros_a)

talo = Talo(1, 10 ,3)
talo.aja_hissia(0, 5)
print(f"Hissi 0 on nyt kerroksessa {talo.hissit[0].kerros}")

talo.aja_hissia(1, 8)
print(f"Hissi 1 on nyt kerroksessa {talo.hissit[1].kerros}")

talo.aja_hissia(2, 3)
print(f"Hissi 2 on nyt kerroksessa {talo.hissit[2].kerros}")

talo.palohalytys()