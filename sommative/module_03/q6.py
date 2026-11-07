# Question 6 : frais de stationnement

import math

electrique = input("Le véhicule est-il électrique ? (oui/non) : ").lower()
duree = float(input("Nombre d'heures de stationnement : "))

# math.ceil arrondit vers le haut : 2.3 h devient 3 h
heures_facturees = math.ceil(duree)

# Il faut payer au moins 1 heure
if heures_facturees < 1:
    heures_facturees = 1

# Première heure : 4.00 $, chaque heure en plus : 2.50 $
prix = 4.00 + (heures_facturees - 1) * 2.50

# Le prix ne peut pas dépasser 20.00 $
if prix > 20.00:
    prix = 20.00

# Rabais de 20 % pour un véhicule électrique
if electrique == "oui":
    rabais = prix * 0.20
else:
    rabais = 0.00

total = prix - rabais

print(f"Durée : {duree} heures")
print(f"Heures facturées : {heures_facturees}")
print(f"Prix avant rabais : {prix:.2f} $")
print(f"Rabais véhicule électrique : {rabais:.2f} $")
print(f"Total : {total:.2f} $")
