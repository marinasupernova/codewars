def count_deaf_rats(town):

    deaf_rats_counter = 0
    town = town.replace(" ", "")
    rats_must_go_right, rats_must_go_left = town.split("P")

    i = 0

    while i < len(rats_must_go_left)-1:
        rat = rats_must_go_left[i] + rats_must_go_left[i+1]
  
        if rat == "~O":
            deaf_rats_counter += 1
        i += 2


    i = 0
    while i < len(rats_must_go_right)-1:
        rat = rats_must_go_right[i] + rats_must_go_right[i+1]
        if rat == "O~":
            deaf_rats_counter += 1
        i += 2


    
    return deaf_rats_counter




print(count_deaf_rats("~O~O~O~O P"))
print(count_deaf_rats("P O~ O~ ~O O~"))
print(count_deaf_rats("~O~O~O~OP~O~OO~"))