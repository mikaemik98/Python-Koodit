Käyttäjätunnus = 'python'
Salasana = 'rules'
yritys = 0
yritys_maara = 5
while yritys <= yritys_maara:
    yritys_maara += 1
    Käyttäjätunnus = input('Anna käyttäjätunnus: ')
    if Käyttäjätunnus == 'python':
        Salasana = input('Anna salasana: ')
        if Salasana == 'rules':
            print('Tervetuloa!')
        elif yritys_maara > 5:
            break
        elif Käyttäjätunnus or Salasana != Käyttäjätunnus or Salasana:
            print('Pääsy evätty')
    else:
        print('Pääsy evätty.')