def max_odd(elem_list: list) -> int:
    max_odd_elem = 0
    for i in elem_list:
        if isinstance(i, (int, float)):
            if i % 2 != 0 and i > max_odd_elem:
                max_odd_elem = int(i)

    if max_odd_elem != 0:
        return max_odd_elem
