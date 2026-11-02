# Question 2 : conversion d'âge

nom = input("Quel est votre nom ? ")
age = input("Quel est votre âge ? ")

# input() donne toujours du texte, même pour l'âge.
# On le change en nombre entier avec int() pour pouvoir faire + 5.
age = int(age)

print(f"{nom}, dans 5 ans, tu auras {age + 5} ans.")
