# Question 2 : conversion de température

# float() accepte les nombres entiers et les nombres à virgule
celsius = float(input("Entrez une température en Celsius : "))

# -273.15 °C est la température la plus froide possible
if celsius < -273.15:
    print("Erreur : la température ne peut pas être plus basse que -273.15 °C.")
else:
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15

    print(f"{celsius:.2f} °C = {fahrenheit:.2f} °F = {kelvin:.2f} K")
