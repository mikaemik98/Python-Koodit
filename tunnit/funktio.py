'''def do_something():
    print('Doing')
    print('something')
    return 'tässä on palautettava arvo, voi olla minkä tyyppinen vaan'

return_value = do_something()
print(return_value)'''
import random

''''#funktio, jolla parametreja (argumentteja)
def combine_strings(string1, string2):
    combination = f'{string1}, {string2}'
    #print(combination)
    return combination

print(combine_strings('auto', 'ajaa'))

combination = combine_strings('kuski', 'jarruttaa')
combination = combine_strings(combination, 'nopeasti')
print(combination)
'''
'''
#yksinkertainen laskin, jolle voi antaa vain tasan 3 parametria
def calculate(calc_type, number1, number2):
    if calc_type == 'sum':
        return number1 + number2
    elif calc_type == 'division':
        return number1 / number2
    #return None # oletustoiminnallisuus

print(calculate('sum', 2.4, 3.5))
print(calculate('division', 2.4, 8))
'''

'''
#ohjelma komentorivikäyttöliittymä
#valikkosovellus yllä esimerkit
#lisätty funktio
def noppa_game():
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

def Ok_app():
    max_count = int(input('Monta kertaa?: '))
    counter = 0
    while counter < max_count:
        counter = counter + 1
        print(f'{counter}. kerran Ok')
    print(f'Laskurin arvo lopuksi: {counter}')

command = ''
while command != 'lopeta':
    command = input('Komento, kiitos> ')
    if command == 'lopeta':
        print('Lopetetaan ohjelma.')
        #break# 'heittää ulos' silmukasta, ei näin
    elif command == 'Ok':
        Ok_app()
    elif command == 'noppa':
        noppa_game()
    else:
        print('En ymmärrä tätä komentoa yritä uudestaan')

print('Ohjelma sammutettu.')
'''

def calculate_sum(numbers):
    total_sum = 0
    #kaksi tapaa tehdä for-loop listan käsittelyyn
    for i in range(len(numbers)):
        total_sum = total_sum + numbers[i]
        numbers[i] = 0 #nollataan listan käsiteltävä alkio ihan vaan huvikseen
    print(numbers)
    #for num in numbers:
    #    total_sum = total_sum + num
    return total_sum


nums = [3, 4, 5]
print(nums)
print(calculate_sum(nums))
print(nums)
#print(calculate_sum([3, 4, 5, 10]))