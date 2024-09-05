import math

def pizzan_hinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * (sade ** 2)
    pinta_ala_neliometreina = pinta_ala / 1000
    yksikkohinta = hinta / pinta_ala_neliometreina
    return yksikkohinta

pizzat = []
for pizza in range(2):
    halkaisija = float(input(f'Anna pizzzan {pizza+1} halkaisija (cm): '))
    hinta = float(input(f'Anna pizzan {pizza+1} hinta euroina: '))
    yksikkohinta = pizzan_hinta(halkaisija, hinta)
    pizzat.append((halkaisija, hinta, yksikkohinta))

for i, pizza in enumerate(pizzat):
    print(f'Pizzan {i+1} yksikköhinta on: {pizza[2]:.2f} euroa per neliometri.')

if pizzat[0][2] < pizzat[1][2]:
    print('Ensimmäinen pizza on edullisempi.')
elif pizzat[0][2] > pizzat[1][2]:
    print('Toinen pizza on edullisempi.')
else:
    print('Pizzat ovat saman hintaisia.')