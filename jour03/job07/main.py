def langue(langage):
    if langage == "javascript":
        return "tu es un développeur web"
    elif langage == "python":
        return "tu es un développeur IA"
    elif langage == "java":
        return "tu es un développeur logiciel"
    else:
        return "Erreur : cas non traité"

langage = input("Entrez un langage : ")

result = langue(langage)
print(result)