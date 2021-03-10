
def find_short(s):
    words = s.split(" ")

    min_letter = float("inf")

    for word in words:
        if len(word) < min_letter:
            min_letter = len(word)
    
    return min_letter