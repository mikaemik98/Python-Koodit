class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        # nykyinen kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros > self.kerros:
            # olion omia metodeita kutsuttuaessa käytetään self.
            while kohdekerros > self.kerros:
                self.kerros_ylos()
            elif kohdekerros < self.kerros:
                self.kerros_alas()

    def kerros_ylos(self):
        self.kerros += 1

    def kerros_alas(self):
        self.kerros -= 1

h = Hissi(2, 10)
h.siirry_kerrokseen(4)
print(h.kerros)
h.siirry_kerrokseen(1)
print(h.kerros)