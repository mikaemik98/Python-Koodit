import math

luku1 = int(input("Anna eka kokonaisluku: "))
luku2 = int(input("Anna toka kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

print(f"Lukujen summa on: {summa}")
print(f"Lukujen tulo on : {tulo}")
print(f"Lukujen keskiarvo on : {keskiarvo:.2f}")