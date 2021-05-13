def find_children(dancing_brigade):
    if dancing_brigade == "":
        return ""
    complete_family = ""
    parents = []
    children = []

    for person in dancing_brigade:
        if person.isupper():
            parents.append(person)
        else:
            children.append(person)
    
    parents.sort()

    for parent in parents:
        complete_family += parent
        for child in children:
            if child == parent.lower():
                complete_family += child

    return complete_family


print(find_children("abBA"))
print(find_children("AaaaaZazzz"))
print(find_children("CbcBcbaA"))
print(find_children("xXfuUuuF"))
print(find_children(""),"")