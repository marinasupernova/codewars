def high(string):

    words = string.split(" ")
    max_count = 0
    max_word = ""

    for word in words:
        if letter_count(word) > max_count:
            max_count = letter_count(word)
            max_word = word

    return max_word

def letter_count(word):
    ab_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    counter = 0

    for letter in word:
        counter += ab_list.index(letter) + 1
    return counter

print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))
print(high('aa b'))
print(high('b aa'))
print(high('bb d'))
print(high('d bb'))
print(high("aaa b"))
print(high("aaa aaa"))

sum(ord(c) - 96

def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))