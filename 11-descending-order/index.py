def descending_order(num):
    descending_list = []
    num_list = str(num)
    i=0

    length = len(num_list)

    while i < length:
        if num_list[i] > num_list[i+1]:
            descending_list.append(num_list[i])
        i+= 1
        
    return descending_list 

print(descending_order(123456789))