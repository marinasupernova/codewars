import unittest
from codewars_unittest import CodewarsTestRunner

unittest.main(testRunner=CodewarsTestRunner())

def to_nato(words):
    if words == "":
        return ""

    nato_decoded = ""

    dictionary = {'A':'Alfa', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'H':'Hotel', 'I':'India', 'J':'Juliett', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}
    
    for letter in words:
        if letter.upper() in dictionary:
            nato_decoded += dictionary[letter.upper()] + " "
        else:
            nato_decoded += letter + " "
    
    nato_decoded = nato_decoded.replace("  ", " ")
    nato_decoded = nato_decoded.replace("  ", " ")

    if nato_decoded[-1] == " ":
        nato_decoded = nato_decoded[:-1]
    return nato_decoded



test.describe("Basic Tests")
test.assert_equals(to_nato('If you can read'), "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta")
test.assert_equals(to_nato('Did not see that coming'), "Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf")
test.assert_equals(to_nato('.d?d!'),'. Delta ? Delta !')