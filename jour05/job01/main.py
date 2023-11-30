longueur = int(input("Entrez la longueur du rectangle : "))
largeur = int(input("Entrez la largeur du rectangle : "))

for i in range(largeur):
    if i == 0 or i == largeur - 1:
        print("|" + "-" * (longueur - 2) + "|||")
    else:
        print("|" + " " * (longueur - 2) + "|")

