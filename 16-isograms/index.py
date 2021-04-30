def is_isogram(string):

    string = string.lower()
    char_counter = {}
    for char in string:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1      
    for key in char_counter:
        if char_counter[key] > 1:
            return False

    return True

print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("moOse"))