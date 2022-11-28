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


#print(coincidence([1, 2, 3, 4, 5], range(3, 6))) # => [3, 4, 5]
#print(coincidence([1, 2, 3, 4, 5])) # => [3, 4, 5]
#print(coincidence()) # => []
#print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))) # => [1, 2, 2.5]