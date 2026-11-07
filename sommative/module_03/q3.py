# Question 3 : facture avec rabais et taxes

montant = float(input("Montant de l'achat avant taxes : "))

# On choisit le rabais selon le montant
if montant < 50:
    rabais = 0
elif montant <= 100:
    rabais = 5
else:
    rabais = 10

economie = montant * rabais / 100
sous_total = montant - economie
taxe = sous_total * 0.13          # TVH de 13 % sur le montant après rabais
total = sous_total + taxe

print(f"Montant initial : {montant:.2f} $")
print(f"Rabais : {rabais} %")
print(f"Montant économisé : {economie:.2f} $")
print(f"Sous-total après rabais : {sous_total:.2f} $")
print(f"TVH (13 %) : {taxe:.2f} $")
print(f"Total final : {total:.2f} $")
