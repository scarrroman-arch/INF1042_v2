# Problème 1 : générateur d'identifiant et de mot de passe

import random


def caracteres_aleatoires(nombre):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
    resultat = ""
    for i in range(nombre):
        resultat += random.choice(caracteres)  # ajoute 1 caractère au hasard
    return resultat


prenom = input("Prénom : ")
nom = input("Nom : ")
annee = input("Année de naissance : ")
ville = input("Ville : ")

# lower() met le texte en minuscules
identifiant = f"{prenom.lower()}.{nom.lower()}@{ville.lower()}.ca"

# Mot de passe : 2 premières lettres du prénom + 2 premières lettres du nom
# + 2 derniers chiffres de l'année + 4 caractères au hasard
mot_de_passe = prenom[:2] + nom[:2] + annee[-2:] + caracteres_aleatoires(4)

print(f"Identifiant : {identifiant}")
print(f"Mot de passe : {mot_de_passe}")
