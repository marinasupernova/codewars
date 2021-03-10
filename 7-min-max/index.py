def max(lst):
    max_value = float("-inf")

    for elem in lst:
        if elem > max_value:
            max_value = elem
    return max_value

def min(lst):
    min_value = float("inf")

    for elem in lst:
        if elem < min_value:
            min_value = elem
    return min_value

def min_max(lst):
    min_value = min(lst)
    max_value = max(lst) 
    return [min_value, max_value]
  
