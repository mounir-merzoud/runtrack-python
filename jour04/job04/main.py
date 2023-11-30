def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange"]
    fruits.insert(2, "mangue")
    return fruits


fruits = ajouter_mangue()
print(fruits)