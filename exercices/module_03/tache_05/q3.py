# Question 3 : logique et priorités

taille = 135
age = 13
a_interdiction = False

# Python fait le "and" avant le "or".
# Les parenthèses obligent Python à vérifier le "or" en premier.
if (taille >= 140 or age >= 12) and not a_interdiction:
    print("Accès permis")
else:
    print("Accès refusé")
