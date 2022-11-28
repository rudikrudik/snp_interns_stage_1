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
