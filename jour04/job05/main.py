
def mettre_a_jour_liste():
    L = [1, 2, 3, 4, 5]
    L[3] = L[2] + L[4]
    return L
L = mettre_a_jour_liste()
deuxieme_valeur = L[1]
print("La deuxième valeur de la liste est :", deuxieme_valeur)


print(L)
