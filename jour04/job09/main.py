def valeur_maximale_minimale_somme():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    valeur_maximale = max(L)
    valeur_minimale = min(L)
    somme_elements = sum(L)
    
    return valeur_maximale, valeur_minimale, somme_elements


resultats = valeur_maximale_minimale_somme()
print("Valeur maximale :", resultats[0])
print("Valeur minimale :", resultats[1])
print("Somme des éléments :", resultats[2])



