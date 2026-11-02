# Question 3 : évaluation d'une note

note = float(input("Entrez la note de l'élève : "))

if note >= 60:
    print("Réussite")
elif note >= 50:
    print("Rattrapage")
else:
    print("Échec")
