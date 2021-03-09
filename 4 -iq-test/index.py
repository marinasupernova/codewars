def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def iq_test(numbers):

    numbers = list(map(lambda x: int(x) , numbers.split(" ")))
    marker = False

    if is_even(numbers[0])  == is_even(numbers[1]):
        marker = is_even(numbers[0])
    else:
        marker = is_even(numbers[2])
    
    for i, num in enumerate(numbers):
        if is_even(num) != marker:
            return i+1
 





        


print(iq_test("2 4 7 8 10"))


# iq_test("2 4 7 8 10") => 3
# iq_test("1 2 1 1") => 2