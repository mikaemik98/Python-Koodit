import random
arpa = random.randint(1, 10)
arvaus = 0
while arvaus != arpa:
    arvaus = int(input('Anna arvaus väliltä 1-10: '))
    if arvaus > arpa:
        print(f'Liian suuri arvaus.')
    elif arvaus < arpa:
        print(f'Liian pieni arvaus.')
    if arvaus == arpa:
        print(f'Oikein!')