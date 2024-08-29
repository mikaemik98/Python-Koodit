import random

#TODO: kysy N arvo käyttäjältä
N = 100
n = 0
iterator = 0
while iterator < N:
    iterator += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f'Arvottu piste: {x}, {y}')
    if x**2 + y**2 < 1:
        print('Piste on yksikköympyrässä.')
        #TODO: lisää n arvoon 1
#TODO: tulosta kaavan mukaan laskettu piin likiarvo