def kokonaisluvut(lukuja):
    parilliset = [luku for luku in lukuja if luku % 2 == 0]
    return parilliset

lista = []
n = int(input('Kuinka monta kokonaislukua haluat antaa?: '))

for i in range(n):
    luku = int(input('Anna luku: '))
    lista.append(luku)
karsittu_lista = kokonaisluvut(lista)

print(f'Alkuperäinen lista: {lista}')
print(f'Karsittu lista, missä vain parilliset: {karsittu_lista}')