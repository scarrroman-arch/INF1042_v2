# Question 4 : débogage et correction
#
# Les 3 erreurs :
# 1. Il manque les deux-points (:) à la fin de la ligne du if.
# 2. Les deux print() doivent être décalés de 4 espaces sous le if et le else.
# 3. « est_etudiant == True » est inutile : est_etudiant vaut déjà True ou False.
#    On écrit simplement « est_etudiant ».

age = 20
est_etudiant = True

if age >= 18 and est_etudiant:
    print("Tarif étudiant disponible")
else:
    print("Plein tarif")
