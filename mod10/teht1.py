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

h = Hissi(2, 10)
h.siirry_kerrokseen(5)
print(h.kerros)
h.siirry_kerrokseen(2)
print(h.kerros)