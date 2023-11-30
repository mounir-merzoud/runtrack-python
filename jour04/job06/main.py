
def changer_entre_la_premiere_et_la_derniere_valeur():
    ma_liste = [1, 2, 3, 4, 5]
    ma_liste[0], ma_liste[4] = ma_liste[4], ma_liste[0]
    return ma_liste


ma_liste = changer_entre_la_premiere_et_la_derniere_valeur()
print(ma_liste)
