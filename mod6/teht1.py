import random

def heita_noppaa():
    return random.randint(1, 6)

def noppa_game():
        die1 = 0
        roll_counter = 0
        while die1 < 6:
            roll_counter += 1
            die1 = heita_noppaa()
            print(f'{roll_counter}. heiton silmäluvut: {die1}')

noppa_game()