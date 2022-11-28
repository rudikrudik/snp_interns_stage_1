#  Task - Done!

def sort_list(target_list: list) -> list:
    temp_list = []

    if len(target_list) != 0:
        max_in_target_list = max(target_list)
        min_in_target_list = min(target_list)
    else:
        return temp_list

    for i in target_list:
        if i == min_in_target_list:
            temp_list.append(max_in_target_list)

        elif i == max_in_target_list:
            temp_list.append(min_in_target_list)

        elif i != max_in_target_list or i != min_in_target_list:
            temp_list.append(i)

    temp_list.append(min_in_target_list)

    return temp_list


#print(sort_list([])) # => []
#print(sort_list([2, 4, 6, 8])) # => [8, 4, 6, 2, 2]
#print(sort_list([1])) # => [1, 1]
#print(sort_list([1, 2, 1, 3])) # => [3, 2, 3, 1, 1]