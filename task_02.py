#  Task - Done!

def coincidence(list_data=None, range_data=range(0)):
    temp_list = []

    for i in range_data:
        for j in list_data:
            if isinstance(j, (int, float)) and i == round(j):
                temp_list.append(j)
            else:
                continue

    return temp_list
