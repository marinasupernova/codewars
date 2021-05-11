def solve(string):
    ab_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
   "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    vowels = ["a","e","i","o","u"]
    counters = []
    counter = 0
    
    for letter in string:
        if letter not in vowels:
                counter += ab_list.index(letter) + 1      
        elif counter > 0:
            counters.append(counter)
            counter = 0
    
    if counter > 0:
        counters.append(counter)
    
    max_value = max(counters)
    return max_value
    

print(solve("zodiac"))
print(solve("chruschtschov"))
print(solve("khrushchev"))
print(solve("strength"))
print(solve("catchphrase"))
print(solve("twelfthstreet"))
print(solve("mischtschenkoana"))