class Työntekijä:

    työntekijöiden_lukumäärä = 0

    def __init__(self, etunimi, sukunimi):
        Työntekijä.työntekijöiden_lukumäärä = Työntekijä.työntekijöiden_lukumäärä + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")


class Tuntipalkkalainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, tuntipalkka):
        super().__init__(etunimi, sukunimi)
        self.tuntipalkka = tuntipalkka

    def tulosta_tiedot(self):
        # haetaan yliluokan metodin printti
        super().tulosta_tiedot()
        # lisätään oma aliluokan printti
        print(f"Tuntipalkkalaisen palkka: {self.tuntipalkka}€/h")

class Kuukausipalkkalainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        super().__init__(etunimi, sukunimi)
        self.kuukausipalkka = kuukausipalkka

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kuukausipalkkalaisen palkka: {self.kuukausipalkka}€/kk")

työntekijät = []
työntekijät.append(Työntekijä("Viivi", "Virta"))
työntekijät.append(Työntekijä("Ahmed", "Habib"))
työntekijät.append(Tuntipalkkalainen("Pekka", "Pelikaani", 10))
työntekijät.append(Kuukausipalkkalainen("Matti", "Masa", 3500))

for t in työntekijät:
    t.tulosta_tiedot()