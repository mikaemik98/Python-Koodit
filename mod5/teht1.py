import random

arpakuutio_maara = int(input('Anna arpakuutioiden lukumäärä: '))
summa = 0
for i in range (arpakuutio_maara):
    heitto = random.randint(1, 6)
    summa += heitto

print(f'Arpakuutioiden summa on: {summa}')
