def produit_dans_intervalle(liste, borne_min, borne_max):
    produit = 1  # Initialiser le produit à 1
    
    for valeur in liste:
        if borne_min <= valeur <= borne_max:
            produit *= valeur
    
    return produit

# Liste initiale
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Borne minimale et maximale de l'intervalle
borne_min = 25
borne_max = 90

# Appeler la fonction pour calculer le produit dans l'intervalle
resultat_produit = produit_dans_intervalle(L, borne_min, borne_max)

# Afficher le résultat
print(f"Le produit des valeurs de la liste dans l'intervalle [{borne_min}, {borne_max}] est : {resultat_produit}")


