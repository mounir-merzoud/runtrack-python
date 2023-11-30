def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%' and num2 != 0:
        return num1 % num2
    else:
        return "Erreur : Opérateur non valide"

# Appels de la fonction avec différents paramètres
result1 = calcule(20, '+', 35)
print(result1)

result2 = calcule(14, '/', 18)
print(result2)

result3 = calcule(99, '*', 44)
print(result3)
