#  Task - Done!

def max_odd(elem_list: list) -> int:
    max_odd_elem = 0
    for i in elem_list:
        if isinstance(i, (int, float)):
            if i % 2 != 0 and i > max_odd_elem:
                max_odd_elem = int(i)

    if max_odd_elem != 0:
        return max_odd_elem


#print(max_odd([1, 2, 3, 4, 4])) # => 3
#print(max_odd([21.0, 2, 3, 4, 4])) # => 21
#print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) # => 3
#print(max_odd(['ololo', 'fufufu'])) # => None
#print(max_odd([2, 2, 4])) # => None