import math

kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

pinta_ala = kanta * korkeus
piiri = 2 * (kanta + korkeus)

print(f"Suorakulmion pinta-ala on: {pinta_ala:.2f}")
print(f"Suorakulmion piiri on: {piiri:.2f}")
