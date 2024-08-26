kuha = float(input('Anna kuhan pituus senttimetreinä: '))
if kuha >= 37:
    print('Kuha on hyvän mittainen')
elif kuha < 37:
    pituus = 37 - kuha
    print('Kuha on alamittainen. Kuha on', pituus,'cm liian lyhyt. Laske kuha takaisin järveen')