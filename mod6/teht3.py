def polttoaine(gallona):
    return gallona * 3.785

def polttoaine_muuntaja():
    while True:
        luku = float(input('Anna gallona: '))
        if luku < 0:
            print('Luku on negatiivinen sitä ei voi tulostaa')
            break
        litra = polttoaine(luku)
        print(f'Antamasi gallona on {litra:.2f} litraa')
polttoaine_muuntaja()