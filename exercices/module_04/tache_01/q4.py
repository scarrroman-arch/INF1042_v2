# Question 4 : découpage et assemblage (split et join)

phrase = input("Entrez une phrase : ")

# split() coupe la phrase à chaque espace et donne une liste de mots
mots = phrase.split()

# len() compte les éléments de la liste
print(f"Liste de mots : {mots}")
print(f"Nombre de mots : {len(mots)}")

# join() recolle les mots en mettant un tiret entre chacun
resultat = "-".join(mots)
print(f"Phrase avec des tirets : {resultat}")
