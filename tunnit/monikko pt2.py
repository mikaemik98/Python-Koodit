nimet = ['Viivi', 'Ahmed']
numerot = ['050-1234567', '050-7654321']

#print(f'{nimet[0]}, numero: {numerot[0]}')

yhteystiedot = {'Viivi': '050-1234567', 'Ahmed': '050-7654321'}
#print(f"Viivin numero: {yhteystiedot['Viivi']}")
hakusana = input('Puhelinnumerohaku, anna nimi: ')
# listojen avulla, selvitetään ensin oikea indeksi
index = nimet.index(hakusana)
print(f'{hakusana}, numero: {numerot[index]}')

# sanakirjalla, hyödynnetään avainta
print(f'{hakusana}, numero: {yhteystiedot[hakusana]}')

# extraa: moniulotteinen EI TULE TENTTIIN
yhteystiedot = {
    'Viivi': {'puh': '050-1234567', 'osoite': 'pikkutie 15'},
    'Ahmed': {'puh': '050-7654321', 'osoite': 'isotie 1'}
}
print(f'Viivin osoite: {yhteystiedot["Viivi"]["osoite"]}')