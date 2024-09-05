import math

def kokonaisluvut(lukuja):
    summa = 0
    for luku in lukuja:
        summa += luku
    return summa

lista = []
n = int(input('Määritä monta lukua haluat antaa, jotka lasketaan yhteen: '))
for i in range(n):
    lista.append(int(input('Anna luku: ')))
tulos = kokonaisluvut(lista)
print(tulos)
#d