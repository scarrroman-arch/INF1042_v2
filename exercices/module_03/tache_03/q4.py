# Question 4 : validation d'un nombre dans un intervalle

nombre = int(input("Entrez un nombre entier : "))

if nombre > 0 and nombre < 100:
    print("Nombre valide")
else:
    print("Nombre hors limite")
