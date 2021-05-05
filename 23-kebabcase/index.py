def kebabize(string):
    kebab_case_string = ""

    for letter in string:
        if letter.isdigit():
            continue 

        if letter.isupper():
            kebab_case_string += "-" + letter.lower() 
        else:
            kebab_case_string += letter
        
    if "-" in kebab_case_string and kebab_case_string[0] == "-":
        kebab_case_string = kebab_case_string[1:]
        
      

    return kebab_case_string




print(kebabize('myCamelCasedString'))
print(kebabize('myCamelHas3Humps'))
print(kebabize('SOS'))
print(kebabize('42'))
print(kebabize('CodeWars'))