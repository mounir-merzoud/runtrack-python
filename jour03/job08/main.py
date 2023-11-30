def afficher_aliments(type_aliment, saison):
    if type_aliment == "fruits":
        if saison == "hiver":
            print("Orange, mandarine et kiwi")
        elif saison == "ete":
            print("Poire, fraise, cassis")
        else:
            print("Saison non reconnue.")
    elif type_aliment == "legume":
        if saison == "hiver":
            print("Carotte, topinambour, endive")
        elif saison == "ete":
            print("Artichaut, aubergine, navet")
        else:
            print("Saison non reconnue.")
    else:
        print("Type d'aliment non reconnu.")

afficher_aliments("fruits", "hiver")
afficher_aliments("fruits", "ete")
afficher_aliments("legume", "hiver")
afficher_aliments("legume", "ete")
