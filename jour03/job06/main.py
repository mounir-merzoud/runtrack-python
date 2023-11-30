def display_positive_or_negative_or_null(number):
    if number > 0:
        return "positif"
    elif number < 0:
        return "negatif"
    elif number == 0:
        return "le nombre est null"
    else:
        return "Erreur : cas non traité"

valeur_number = int(input("Entrez un nombre : "))
result = display_positive_or_negative_or_null(valeur_number)
print(result)
