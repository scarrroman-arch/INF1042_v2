# Question 5 : jeu Pierre, papier, ciseaux

import random

choix_possibles = ["pierre", "papier", "ciseaux"]

victoires = 0
defaites = 0
egalites = 0

while True:
    joueur = input("Pierre, papier ou ciseaux ? (quitter pour arrêter) : ").lower()

    if joueur == "quitter":
        break

    # Un choix invalide ne compte pas comme une partie
    if joueur not in choix_possibles:
        print("Choix invalide, essayez encore.")
        continue

    ordinateur = random.choice(choix_possibles)
    print(f"Vous : {joueur} | Ordinateur : {ordinateur}")

    if joueur == ordinateur:
        print("Égalité !")
        egalites += 1
    # Pierre bat ciseaux, ciseaux battent papier, papier bat pierre
    elif (joueur == "pierre" and ordinateur == "ciseaux"
          or joueur == "ciseaux" and ordinateur == "papier"
          or joueur == "papier" and ordinateur == "pierre"):
        print("Vous gagnez !")
        victoires += 1
    else:
        print("Vous perdez.")
        defaites += 1

print()
print(f"Victoires : {victoires}")
print(f"Défaites : {defaites}")
print(f"Égalités : {egalites}")
print(f"Total de parties : {victoires + defaites + egalites}")
