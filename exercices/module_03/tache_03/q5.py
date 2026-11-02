# Question 5 : choix aléatoire avec random

import random

options = ["Pierre", "Papier", "Ciseaux"]
choix_ordinateur = random.choice(options)

choix_utilisateur = input("Votre choix (Pierre, Papier ou Ciseaux) : ")

print(f"L'ordinateur a choisi : {choix_ordinateur}")

if choix_utilisateur == choix_ordinateur:
    print("Égalité !")
else:
    print("Choix différents !")
