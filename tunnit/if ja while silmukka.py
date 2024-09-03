import random
'''
print(not True)
print(True and True)
print(True and False)
print(True or True)
print(True and (False or True))
result = (False or False) and (False or True)
print(f'Vertailu tulos: {result}')
print( 1 < 2 or (1 == 1 and result))
'''
#while-silmukka
#ikuinen silmukka,ei näin
'''
while True:
    print('Moi')
    print('Mikael')
'''

'''
max_count = int(input('Monta kertaa?: '))
counter = 0
while counter < max_count:
    counter = counter + 1
    print(f'{counter}. kerran Ok')
print(f'Laskurin arvo lopuksi: {counter}')
'''
'''
#noppasimulaattori
#mikä on kahden yhtäaikaisen kutosen todennäköisyys?
rounds = 1000
round_counter = 0
total_rolls = 0
while round_counter < rounds:
    round_counter += 1
    die1 = 0
    die2 = 0
    roll_counter = 0
    while die1 < 6 or die2 <6:
        roll_counter += 1
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        #print(f'{roll_counter}. heiton silmäluvut: {die1} ja {die2}')
    #print(f'Noppaa heitettiin {roll_counter} kertaa.')
    total_rolls = total_rolls + roll_counter
print(f'Kaksi kutosta saatiin keskimäärin {total_rolls / rounds} heitolla')
'''

#ohjelma komentorivikäyttöliittymä
#valikkosovellus yllä esimerkit
#lisätty funktio
command = ''
while command != 'lopeta':
    command = input('Komento, kiitos> ')
    if command == 'lopeta':
        print('Lopetetaan ohjelma.')
        #break# 'heittää ulos' silmukasta, ei näin
    elif command == 'Ok':
        max_count = int(input('Monta kertaa?: '))
        counter = 0
        while counter < max_count:
            counter = counter + 1
            print(f'{counter}. kerran Ok')
        print(f'Laskurin arvo lopuksi: {counter}')
    elif command == 'noppa':
        rounds = 1000
        round_counter = 0
        total_rolls = 0
        while round_counter < rounds:
            round_counter += 1
            die1 = 0
            die2 = 0
            roll_counter = 0
            while die1 < 6 or die2 < 6:
                roll_counter += 1
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                # print(f'{roll_counter}. heiton silmäluvut: {die1} ja {die2}')
            # print(f'Noppaa heitettiin {roll_counter} kertaa.')
            total_rolls = total_rolls + roll_counter
        print(f'Kaksi kutosta saatiin keskimäärin {total_rolls / rounds} heitolla')
    else:
        print('En ymmärrä komentoa. Yritä uudestaan, kiitos')

print('Ohjelma sammutettu.')