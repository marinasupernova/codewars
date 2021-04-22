def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    result = []
    min_num = min(numbers)
    is_firstremoved = False

    for elem in numbers:
        
        if elem == min_num and is_firstremoved == False:
            is_firstremoved = True
        else:
            result.append(elem)

    return result



print(remove_smallest([1, 2, 3, 4, 5]))
print(remove_smallest([5, 3, 2, 1, 4]))

print(remove_smallest([1, 2, 3, 1, 1]))
print(remove_smallest([]))




# def remove_smallest(numbers):
#     min_num = min(numbers)

#     for index, elem in enumerate(numbers):
#         for min_num in numbers[index+1:]:
#             compare (elem, min(number))
#     return result


# print(remove_smallest([1, 2, 3, 1, 1]))