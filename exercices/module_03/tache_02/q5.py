# Question 5 : partage de bonbons

bonbons = 53
eleves = 8

part = bonbons // eleves  # bonbons pour chaque élève
reste = bonbons % eleves  # bonbons qui restent

print(f"Chaque élève reçoit {part} bonbons.")
print(f"Il reste {reste} bonbons.")
print(f"53 / 8 = {bonbons / eleves}")

# Explication :
# // donne 6 : chaque élève reçoit 6 bonbons entiers.
# % donne 5 : il reste 5 bonbons.
# / donne 6.625 : c'est comme si on coupait les bonbons en morceaux.
print("Avec // et %, on obtient 6 bonbons chacun et il en reste 5.")
print("Avec /, on obtient 6.625, mais on ne peut pas donner un morceau de bonbon.")
