def my_sort(lst):
    # Initialisation du nombre total de coups
    total_coups = 0
    # Variable pour indiquer si un échange a été effectué lors du passage
    swapped = True

    # Boucle principale
    while swapped:
        swapped = False
        # Parcours de la liste
        for i in range(len(lst) - 1):
            # Comparaison des éléments adjacents
            if lst[i] > lst[i + 1]:
                # Échange des éléments s'ils ne sont pas dans l'ordre croissant
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
                # Incrémentation du nombre de coups
                total_coups += 1

    # Affichage de la liste triée et du nombre total de coups
    print("Liste triée:", lst)
    print("Nombre total de coups nécessaires:", total_coups)
    
    # Retour de la liste triée
    return lst

# Exemple d'utilisation :
ma_liste = [4, 2, 7, 1, 9, 5]
my_sort(ma_liste)
