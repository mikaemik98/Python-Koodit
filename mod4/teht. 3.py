luvut = []
luku = input('Syötä luku: ')
while luku != '':
    luvut.append(int(luku))
    print(f'Syötit luvun: {luku}')
    luku = input('Syötä luku: ')
if luvut:
    print(f'Annoit tyhjän merkkijonon, ohjelma lopetetaan. Suurin antamasi luku oli {max(luvut)} ja pienin antamasi luku oli  {min(luvut)}')