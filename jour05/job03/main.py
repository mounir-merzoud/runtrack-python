L = 5
for i in range(L):
    for j in range(L - i - 1):
        print(" ", end='')  # Ajoutez des espaces à gauche

    if i == L - 1:
        print("/", end='')  # Premier caractère de la dernière ligne
        for k in range(2 * i):
            print("_", end='')  # Caractère '_' pour la dernière ligne
        print("\\", end='')  # Dernier caractère de la dernière ligne
    else:
        print("/", end='')  # Premier caractère de chaque ligne
        for k in range(2 * i):
            print(" ", end='')  # Ajoutez des espaces au milieu
        print("\\", end='')  # Dernier caractère de chaque ligne

    print()  # Passer à une nouvelle ligne après chaque ligne du triangle