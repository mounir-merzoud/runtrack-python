def verifier_pair_impair():
    entree_utilisateur = input("Entrez un nombre entier positif : ")

    try:
        nombre = int(entree_utilisateur)
        if nombre >= 0:
            if nombre % 2 == 0:
                return f"{nombre} est Pair"
            else:
                return f"{nombre} est Impair"
        else:
            return "Veuillez entrer un nombre entier positif."
    except ValueError:
        return "Veuillez entrer un nombre entier valide."
resultat = verifier_pair_impair()
print(resultat)

