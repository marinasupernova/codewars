def count(string):

    output = {}

    for char in string:

        if char in output: 
            output[char] += 1
        else:
            output[char] = 1
    return output



print(count('hvghjhkjkloopopki'))
print(count(''), {})