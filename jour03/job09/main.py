def moyenne():
    premiere_moyenne = float(input("Entrez la première moyenne : "))
    deuxieme_moyenne = float(input("Entrez la deuxième moyenne : "))
    troisieme_moyenne = float(input("Entrez la troisième moyenne : "))
    moyene = (premiere_moyenne + deuxieme_moyenne + troisieme_moyenne) / 3

    if 0 <= moyene <= 7:
        print("Élève devant faire des efforts.")
    elif 8 <= moyene <= 10:
        print("Élève moyen.")
    elif 11 <= moyene <= 14:
        print("Bon élève.")
    elif 15 <= moyene <= 20:
        print("Très bon élève.")
    else:
        print("Moyenne invalide. Assurez-vous que les notes sont entre 0 et 20.")

# Appeler la fonction pour calculer la moyenne et afficher le résultat
moyenne()
