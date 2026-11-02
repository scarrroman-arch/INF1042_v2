# Question 4 : convertir un nombre à virgule en entier

x = 7.8

y = int(x)    # int() enlève les chiffres après la virgule (il n'arrondit pas)
diff = x - y  # ce qui a été enlevé

print(f"y = {y}")
print(f"diff = {diff:.2f}")
