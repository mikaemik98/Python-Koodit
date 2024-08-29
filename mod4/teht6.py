import random

N = 100
iterator = 0
while iterator < N:
    iterator += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f'Arvottu piste: {x}, {y}')