def letter_count(string):

    letters = {}

    for letter in string:
        letters[letter] = 0

    for letter in string:
        letters[letter] += 1

    return letters

# from collections import Counter
# def letter_count(s):
#     return Counter(s)

print(letter_count("codewars"))
print(letter_count("activity"))
print(letter_count("arithmetics"))
print(letter_count("traveller"))
print(letter_count("daydreamer"))