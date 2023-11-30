def multiple_3():
    L = [8, 24,48,2,16]
    compter = 0
    for i in L:
        if i %3 == 0:
            compter += 1 
    return compter

print(multiple_3())