def divisors(integer):
    divisors_list = []

    for n in range(2, integer):
        if integer % n == 0:
            divisors_list.append(n)
    
    if len(divisors_list) == 0:
        return str(integer) + " is prime"

    return divisors_list


print(divisors(17))    