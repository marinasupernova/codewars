def wave(string):
    mexican_wave = []
    real_mexican_wave = []

    for letter in string:
        if letter != " ":
            mexican_wave.append(list(string))

    i = 0
    length = len(mexican_wave)

    while i < length:
        mexican_wave[i][i] = mexican_wave[i][i].upper()
        i += 1
    
    for letters in mexican_wave:
      real_mexican_wave.append("".join(letters))

    return real_mexican_wave

# print(wave("hello"))
print(wave("Two words"))

https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
    