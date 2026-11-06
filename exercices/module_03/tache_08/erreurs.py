# Tâche 08 : programme de fidélité et d'épargne (corrigé)


def calculer_prix_rabais(prix_initial, type_client):
    if type_client == "VIP":
        rabais = 0.20
    elif type_client == "Membre":
        rabais = 0.10
    else:
        rabais = 0.00

    # Correction 1 : on enlève 20 % du prix, pas 0.20 $
    prix_final = prix_initial - prix_initial * rabais
    return prix_final


def calculer_points_accumules(nombre_achats, points_par_achat):
    total_points = 0

    # Correction 2 : + 1 pour faire 5 tours au lieu de 4
    for i in range(1, nombre_achats + 1):
        total_points += points_par_achat

    return total_points


def calculer_epargne_avec_bonus(montant_mensuel, nombre_mois):
    total = 0.0
    mois_actuel = 1

    # Correction 4 : <= pour compter aussi le dernier mois
    while mois_actuel <= nombre_mois:
        # Correction 3 : += pour ajouter au total au lieu de le remplacer
        total += montant_mensuel + 5
        mois_actuel += 1

    return total


# --- TESTS ---
if __name__ == "__main__":
    print("=== TEST 1 : Prix avec rabais VIP ===")
    prix_vip = calculer_prix_rabais(50.00, "VIP")
    print(f"Prix obtenu     : {prix_vip:.2f} $(Attendu : 40.00$)")

    print("\n=== TEST 2 : Points de fidélité (5 achats de 10 points) ===")
    points = calculer_points_accumules(nombre_achats=5, points_par_achat=10)
    print(f"Points obtenus  : {points} (Attendu : 50 points)")

    print("\n=== TEST 3 : Épargne sur 4 mois (50$+ 5$ bonus / mois) ===")
    epargne = calculer_epargne_avec_bonus(montant_mensuel=50.00, nombre_mois=4)
    print(f"Épargne obtenue : {epargne:.2f} $(Attendu : 220.00$)")
