def resultat(note):
    if note < 40:
        print("Grosse merde")
    else:
        if note % 5 and note % 5 > 2:
            note += 5 - (note % 5)
        print("Test réussi ! Note : ", note)

resultat(86)