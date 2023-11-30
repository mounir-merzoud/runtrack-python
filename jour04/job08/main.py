def somme_des_valeurs_paires():
    L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    somme_paires = 0  

    for i in L:
        if i % 2 == 0:
            somme_paires += i 
    return somme_paires  
resultat_somme_paires = somme_des_valeurs_paires()
print("La somme des valeurs paires est :", resultat_somme_paires)
