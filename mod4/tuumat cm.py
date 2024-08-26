tuuma = 2.54
while True:
    luku = float(input('Anna tuuma: '))
    if luku < 0:
        print('Luku on negatiivinen sitä ei voi tulostaa')
        break
    cm = tuuma * luku
    print(f'Antamasi tuuma on {cm}cm')


