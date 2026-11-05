# Question 5 : fonction qui calcule l'aire d'un cercle

import math


def aire_cercle(diametre):
    rayon = diametre / 2
    aire = math.pi * rayon ** 2  # aire = pi x rayon au carré
    return aire


resultat = aire_cercle(10)

print(f"Aire d'un cercle de diamètre 10 : {resultat:.2f}")
