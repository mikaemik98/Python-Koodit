import random

N = 100
n = 0
iterator = 0
while iterator < N:
    N = int(input('Anna arvottavien pisteiden määrä: '))
    iterator += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f'Arvottu piste: {x}, {y}')
    if x**2 + y**2 < 1:
        n += 1
        iterator += 1
        print('Piste on yksikköympyrässä.')
    pi_likiarvo = 4 * n/N
    print(f'Piin likiarvo on: {pi_likiarvo}')