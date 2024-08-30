Kayttajatunnus_O = 'python'
Salasana_O = 'rules'
yritys = 0
yritys_maara = 5
while yritys < yritys_maara:
    yritys += 1
    Kayttajatunnus = input('Anna käyttäjätunnus: ')
    Salasana = input('Anna salasana: ')
    if Kayttajatunnus == Kayttajatunnus_O and Salasana == Salasana_O:
        print('Tervetuloa!')
        break
    else:
        yritys += 1
        if yritys > yritys_maara:
            print('Virheellinen salasana tai käyttäjätunnus.')
        else:
            print('Pääsy evätty.')