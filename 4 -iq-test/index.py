# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False


# def iq_test(numbers):

#     numbers = list(map(lambda x: int(x) , numbers.split(" ")))
#     marker = False

#     if is_even(numbers[0])  == is_even(numbers[1]):
#         marker = is_even(numbers[0])
#     else:
#         marker = is_even(numbers[2])
    
#     for i, num in enumerate(numbers):
#         if is_even(num) != marker:
#             return i+1
 





        


# print(iq_test("2 4 7 8 10"))


# def number(bus_stops):
#     counter = 0

#     for people_on_a_stop in bus_stops:
#         counter += people_on_a_stop[0]
#         counter -= people_on_a_stop[1]
#     return counter


# print(number([[10,0],[3,5],[5,8]]))

def namelist(persons):
    names = []
    output = ""
    
    for person in persons:
        names.append(person['name'])

    if len(names) == 1:
        return names[0]
    elif len(names) == 0:
        return ''
    

    output = ", ".join(names[:-1]) + " & " + names[-1]



    return output





print(namelist([]))
print(namelist ([ {'name': 'Bart'} ]) )
# print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))