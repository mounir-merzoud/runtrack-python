def augmenter_elements_liste():
    L = [7, 11, 42, 39, 2]
    for i in range(len(L)):
        L[i] += 1
    return L
L = augmenter_elements_liste()
print("Liste après la modification :", L)
