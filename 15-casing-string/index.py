def to_jaden_case(string):
    # output = ""
    # words = string.split(" ")
    # for word in words:
    #     output += word[0].upper() + word[1:] + " "     
    # return output

    words = string.split(" ")
    output = " ".join([word[0].upper() + word[1:] for word in words])
    return output

print(to_jaden_case("How can mirrors be real if our eyes aren't real?"))