def solution(string, ending):

    ending_length = len(ending)
    if ending == "":
        return True   
    if ending == string[-ending_length:]:
        return True       
    else:
        return False


print(solution('abcde', 'cde'))
print(solution('abcde', 'abc'))
print(solution('abcde', ''))
print(solution('samurai', 'ai'))
print(solution('sensei', 'i'))



    
    
