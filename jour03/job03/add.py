def perform_operations(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Division par zéro n'est pas autorisée."
    else:
        return "Opération non prise en charge."

# Appels de la fonction avec différents paramètres et opérations
resultat_addition = perform_operations(10, 5, 'add')
resultat_multiplication = perform_operations(3, 4, 'multiply')
resultat_division = perform_operations(8, 2, 'divide')

# Affichage des résultats
print("Résultat de l'addition:", resultat_addition)
print("Résultat de la multiplication:", resultat_multiplication)
print("Résultat de la division:", resultat_division)
