# Question 4 : la date dans 100 heures

from datetime import datetime, timedelta

maintenant = datetime.now()
dans_100_heures = maintenant + timedelta(hours=100)  # timedelta = une durée

# strftime() choisit comment afficher la date : année-mois-jour heure:minutes
print(f"Maintenant : {maintenant.strftime('%Y-%m-%d %H:%M')}")
print(f"Dans 100 heures : {dans_100_heures.strftime('%Y-%m-%d %H:%M')}")
