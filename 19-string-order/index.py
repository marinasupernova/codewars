def order(sentence):

    words = sentence.split(" ")

    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ordered_words = []

    for word in words:
        ordered_words.append("")

    for word in words: 
        for char in word:
            if char in nums:
                index = int(char)
                ordered_words[index-1] = word
    
    return " ".join(ordered_words)




print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))