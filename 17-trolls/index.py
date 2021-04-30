def disemvowel(string_):

    vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I' ]
    clean_msg =[]

    for letter in string_:
        if letter not in vowels: 
            clean_msg.append(letter)

    
    return "".join(clean_msg)

print(disemvowel("This website is for losers LOL!"))