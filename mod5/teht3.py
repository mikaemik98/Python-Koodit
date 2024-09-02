anna_luku = int(input('Anna luku: '))
if anna_luku < 2:
    print(f'Luku {anna_luku} ei ole alkuluku')
else:
    on_alkuluku = True
for luku in range(2, anna_luku):
    if anna_luku % luku == 0:
        on_alkuluku = False
        break
if on_alkuluku:
    print(f'Luku {anna_luku} on alkuluku')
else:
    print(f'Luku {anna_luku} ei ole alkuluku')