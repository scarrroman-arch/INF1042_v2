# ==========================================================
# INF1042 - Module 03 - Tâche 01
# Auteur : Roman Scarr
# Description : Premier script Python qui affiche une
#               présentation de moi-même.
# ==========================================================

# --- Variables (des "boîtes" nommées en mémoire) ---
# Le nom est une chaîne de caractères (str)
nom_complet = "Roman Scarr"

# Le nom du collège et le cours sont aussi des chaînes (str)
college = "Collège Boréal"
cours = "INF1042"

# Une valeur logique (bool) : True ou False
aime_programmer = True

# --- Affichage de la présentation avec print() ---
# Ligne de titre pour séparer visuellement la présentation
print("==============================")
print("     Ma présentation")
print("==============================")

# Affiche le nom en combinant du texte et une variable
print("Bonjour ! Je m'appelle", nom_complet + ".")

# Affiche le collège et le cours
print("J'étudie au", college, "dans le cours", cours + ".")

# Affiche mes intérêts
print("Mes intérêts : les jeux vidéo et la programmation en Python.")

# --- Exemple d'indentation (4 espaces obligatoires) ---
# Le bloc sous le "if" est indenté de 4 espaces
if aime_programmer:
    print("J'aime programmer et j'ai hâte d'en apprendre plus !")

# Message de fin
print("Merci d'avoir lu ma présentation.")
