def sort_names(s):
    sorted_names = "" 
 
    persons = []

    s = s.split(";")

    for elem in s:
        split_name = elem.split(":")
        person = {
            "firstname": split_name[0],
            "lastname": split_name[1]
        }
        persons.append("(" + split_name[1].upper() + ", " + split_name[0].upper() + ")")

    sorted_names = "".join(sorted(persons))

    return sorted_names

print(sort_names("John:Gates;Michael:Wahl;Megan:Bell;Paul:Dorries;James:Dorny;Lewis:Steve;Alex:Meta;Elizabeth:Russel;Anna:Korn;Ann:Kern;Amber:Cornwell")) 
#print(sort_names("Alex:Arno;Alissa:Cornwell;Sarah:Bell;Andrew:Dorries;Ann:Kern;Haley:Arno;Paul:Dorny;Madison:Kern"))
'(ARNO, ANN), (BELL, JOHN), (CORNWELL, ALEX), (DORNY, ABBA), (KERN, LEWIS), (KORN, ALEX), (META, GRACE), (SCHWARZ, VICTORIA), (STAN, MADISON), (STAN, MEGAN), (WAHL, ALEXIS)' should equal 
'(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)'