def alphabet_position(text):

    text = text.lower()

    ab_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
   "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    encoded = []

    for letter in text:
        if letter in ab_list:
            ab_index = ab_list.index(letter)
            encoded.append(ab_index +1)
    
    string_ints = [str(int) for int in encoded] 


    return " ".join(string_ints)



print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))

"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
20 8 5 19 22 14 19 5 20 19 5 20 19 1 20 20 23 5 12 21 5 15 3 12 15 3 11
