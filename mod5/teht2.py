luvut = []

annettu_luku = input('Anna luku tai paina enter lopettaaksesi: ')
while annettu_luku != '':
    luvut.append(int(annettu_luku))
    annettu_luku = input('Anna seuraava luku tai paina enter lopettaaksesi: ')
luvut.sort(reverse=True)
print(f'Viisi suurinta lukua järjestyksessä isoimmasta pienimpään: ')
for i in range(min(5, len(luvut))):
    print(luvut[i])
