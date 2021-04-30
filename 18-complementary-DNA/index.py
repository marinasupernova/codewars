def DNA_strand(dna):
    new_pair = ""
    pairs = {
        "A":"T",
        "T":"A",
        "G":"C",
        "C":"G",
    }
    for letter in dna:
        new_pair += pairs[letter]
    return new_pair




print(DNA_strand("AAAA"))
print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))