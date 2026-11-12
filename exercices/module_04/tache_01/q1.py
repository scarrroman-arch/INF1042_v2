# Question 1 : indexation et découpage (slicing)

phrase = input("Entrez une phrase : ")

# [0] est le premier caractère, [-1] est le dernier
print(f"Premier caractère : {phrase[0]}")
print(f"Dernier caractère : {phrase[-1]}")

# [0:5] prend les caractères de l'index 0 à 4 (le 5 n'est pas inclus)
print(f"Les 5 premiers caractères : {phrase[0:5]}")

# [::-1] lit la phrase de la fin vers le début
print(f"Phrase inversée : {phrase[::-1]}")
