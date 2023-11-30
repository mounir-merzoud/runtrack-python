def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note >= 40 and note % 5 >= 3:
            note_arrondie = note + (5 - note % 5)
            if note_arrondie <= 100:
                notes_arrondies.append(note_arrondie)
            else:
                notes_arrondies.append(note)
        else:
            notes_arrondies.append(note)

    return notes_arrondies


notes_eleves = [43, 83, 92, 64, 53]
notes_arrondies = arrondir_notes(notes_eleves)
print("Notes des élèves:", notes_eleves)
print("Notes arrondies:", notes_arrondies)
