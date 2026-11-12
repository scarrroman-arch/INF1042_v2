# Question 5 : parcourir une chaîne comme un tableau

phrase = input("Entrez une phrase : ")

voyelles = "aeiouy"
nombre_voyelles = 0

# lower() met la phrase en minuscules pour compter aussi A, E, I...
for caractere in phrase.lower():
    if caractere in voyelles:
        nombre_voyelles += 1

print(f"Nombre de voyelles : {nombre_voyelles}")
