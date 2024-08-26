luoti_grammoina = 13.3
naula_luoteina = 32
leiviska_nauloina = 20

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

kokonaismassa_grammoina = (
    leiviskat * leiviska_nauloina * naula_luoteina * luoti_grammoina +
    naulat * naula_luoteina * luoti_grammoina +
    luodit * luoti_grammoina
)

kilogrammat = int(kokonaismassa_grammoina // 1000)
grammat = kokonaismassa_grammoina % 1000

print(f"Massa nykymittojen mukaan: ")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")