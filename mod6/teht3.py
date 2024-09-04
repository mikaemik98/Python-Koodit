def polttoaine(gallona):
    return gallona

def polttoaine_muuntaja():
    while True:
        gallona = 3.785
        luku = float(input('Anna gallona: '))
        if luku < 0:
            print('Luku on negatiivinen sitä ei voi tulostaa')
            break
        litra = gallona * luku
        print(f'Antamasi gallona on {litra} litraa')
polttoaine_muuntaja()