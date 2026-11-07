# Question 4 : simulation de tirages aléatoires entre 1 et 4

import random

nombre_tirages = int(input("Combien de tirages voulez-vous faire ? "))

# Un compteur pour chaque nombre
compte1 = 0
compte2 = 0
compte3 = 0
compte4 = 0

for i in range(nombre_tirages):
    tirage = random.randint(1, 4)
    if tirage == 1:
        compte1 += 1
    elif tirage == 2:
        compte2 += 1
    elif tirage == 3:
        compte3 += 1
    else:
        compte4 += 1

if nombre_tirages > 0:
    print(f"1 : {compte1} fois — {compte1 / nombre_tirages * 100:.1f} %")
    print(f"2 : {compte2} fois — {compte2 / nombre_tirages * 100:.1f} %")
    print(f"3 : {compte3} fois — {compte3 / nombre_tirages * 100:.1f} %")
    print(f"4 : {compte4} fois — {compte4 / nombre_tirages * 100:.1f} %")

    # On cherche le nombre tiré le plus souvent
    plus_souvent = 1
    plus_grand = compte1
    if compte2 > plus_grand:
        plus_souvent = 2
        plus_grand = compte2
    if compte3 > plus_grand:
        plus_souvent = 3
        plus_grand = compte3
    if compte4 > plus_grand:
        plus_souvent = 4
        plus_grand = compte4

    print(f"Le nombre tiré le plus souvent : {plus_souvent}")
else:
    print("Aucun tirage effectué.")
