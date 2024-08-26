sukupuoli = input('Anna biologinen sukupuoli: ')
hemoglobiiniarvo = int(input('Anna hemoglobiiniarvo (g/l): '))
if sukupuoli == 'mies':
    if hemoglobiiniarvo < 134:
        print('Hemoglobiiniarvo alhainen')
    elif 134 <= hemoglobiiniarvo <= 195:
        print('Hemoglobiini arvo normaali')
    elif hemoglobiiniarvo > 195:
        print('Hemoglobiini arvo korkea')
elif sukupuoli == 'nainen':
    if hemoglobiiniarvo < 117:
        print('Hemoglobiiniarvo alhainen')
    elif 117 <= hemoglobiiniarvo <= 175:
        print('Hemoglobiini arvo normaali')
    elif hemoglobiiniarvo > 175:
        print('Hemoglobiini arvo korkea')
else:
    print('Virheellinen sukupuoli')