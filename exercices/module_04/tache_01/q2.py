# Question 2 : nettoyage et conversion de casse

phrase = input("Entrez une phrase avec des espaces au début et à la fin : ")

# strip() enlève les espaces au début et à la fin
phrase = phrase.strip()

print(f"Phrase nettoyée : {phrase}")
print(f"En majuscules : {phrase.upper()}")
print(f"En minuscules : {phrase.lower()}")
