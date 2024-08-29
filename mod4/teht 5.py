Käyttäjätunnus = 'python'
Salasana = 'rules'
while Käyttäjätunnus == 'python':
    Käyttäjätunnus = input('Anna käyttäjätunnus: ')
    if Käyttäjätunnus == 'python':
        Salasana = input('Anna salasana: ')
        if Salasana == 'rules':
            print('Tervetuloa!')
        elif Käyttäjätunnus or Salasana != Käyttäjätunnus or Salasana:
            print('Pääsy evätty')
    else:
        print('Pääsy evätty.')