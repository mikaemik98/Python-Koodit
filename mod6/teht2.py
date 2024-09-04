import random

def heita_noppaa(tahko):
    return random.randint(1, tahko)

def noppa_game():
    command1 = ''
    while command1 != 'lopeta':
        command1 = input('Anna nopan tahkomäärä tai kirjoita "lopeta" lopettaaksesi ohjelma: ')
        if command1 == 'lopeta':
            print('Lopetetaan ohjelma.')
            return
        if command1.isdigit():
            tahko1 = int(command1)
            die1 = 0
            roll_counter = 0

            while die1 != tahko1:
                roll_counter += 1
                die1 = heita_noppaa(tahko1)
                print(f'{roll_counter}. heiton silmäluku: {die1}')

noppa_game()