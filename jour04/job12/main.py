def tri_bulles(liste):
    n = 0
    for _ in liste:
        n += 1

    i = 0
    while i < n:

        j = 0
        while j < n-i-1:
            
            if liste[j] > liste[j+1]:
                
                temp = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = temp
            j += 1
        i += 1

ma_liste = [2, 7, 8, 9, 16, 24, 27, 48, 84, 91, 102]
tri_bulles(ma_liste)

print("Liste triée :", ma_liste)