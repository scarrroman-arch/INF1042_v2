# Problème 2 : jeu de calcul mental chronométré

import random
import time


def calculer(a, operation, b):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    else:
        return a * b


nombre_questions = int(input("Combien de questions voulez-vous ? "))

bonnes = 0
mauvaises = 0
temps_total = 0

for i in range(nombre_questions):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    operation = random.choice(["+", "-", "*"])
    bonne_reponse = calculer(a, operation, b)

    start = time.time()
    reponse = int(input(f"Question {i + 1} : {a} {operation} {b} = "))
    end = time.time()

    temps = end - start
    temps_total += temps

    if reponse == bonne_reponse:
        print(f"Bonne réponse ! ({temps:.2f} secondes)")
        bonnes += 1
    else:
        print(f"Mauvaise réponse. La réponse était {bonne_reponse}. ({temps:.2f} secondes)")
        mauvaises += 1

if nombre_questions > 0:
    temps_moyen = temps_total / nombre_questions
    print()
    print(f"Score final : {bonnes} / {nombre_questions}")
    print(f"Bonnes réponses : {bonnes}")
    print(f"Mauvaises réponses : {mauvaises}")
    print(f"Temps moyen : {temps_moyen:.2f} secondes")
else:
    print("Aucune question posée.")
