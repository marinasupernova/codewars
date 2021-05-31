def is_pangram(string):
    string = string.lower()
    ab_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
   "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lst = []

    for letter in string:
        if letter not in lst and letter in ab_list:
            lst.append(letter)

    if len(lst) != 26:
        return False
    else:
        return True

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram("Cwm fjord bank glyphs vext quiz is a pangram"))

