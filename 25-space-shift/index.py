def get_order(order):
    initial_menu =["burger","fries","chicken","pizza","sandwich","onionrings", "milkshake", "coke"]
    corrected_order = []

    # while len(order) > 0:
    #     for word in initial_menu:
    #         if order[:len(word)] == word:
    #             corrected_order.append(word.capitalize())
    #             order = order[len(word):]
    
    # return " ".join(corrected_order)

    i = 0
    while i < len(initial_menu):
        word = initial_menu[i]
        if word in order:
            print(order)
            corrected_order.append(word)
            order = order [ order.index(word) : order.index(word) + len(word) ]
        else:
            i += 1




print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))
print(get_order("pizzachickenfriesburgercokemilkshakefriessandwich"))
