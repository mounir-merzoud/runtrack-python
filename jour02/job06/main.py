for i in range(2, 1001):
    for n in range(2, 1001):
        if (i == n or i == 2) and n % 2 != 0:
            print(i)
            break



