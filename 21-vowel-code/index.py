def encode(st):

    
    output = st

    output = output.replace("e", "2")
    output = output.replace("a", "1")
    output = output.replace("o", "4")
    output = output.replace("u", "5")
    output = output.replace("i", "3")

    return output
    
def decode(st):
   

    output = st

    output = output.replace("2", "e")
    output = output.replace("1", "a")
    output = output.replace("4", "o")
    output = output.replace("5", "u")
    output = output.replace("3", "i")


    return output



print(encode('hello'))
print(encode('How are you today?'))
print(encode('This is an encoding test.'))
print(decode('h2ll4'))