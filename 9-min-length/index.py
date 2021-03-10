def number(lines):
    output = []

    length = len(lines)
    i = 0

    while i < length: 
        new_value = str(i+1) + ": " + str(lines[i])
        output.append(new_value)
        i+= 1

    return output 
