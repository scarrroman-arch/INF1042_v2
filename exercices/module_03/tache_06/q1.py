# Question 1 : vérifier la longueur du nom

nom = input("Quel est votre nom ? ")

if 8 <= len(nom) <= 12:  # len() compte les lettres du nom
    print("Nom valide")
else:
    print("Erreur : le nom doit avoir entre 8 et 12 caractères.")
