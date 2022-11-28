def combine_anagrams(target_list: list) -> list:
    temp_dict = {}

    for i in target_list:
        key = ''.join(sorted(i))
        if temp_dict.get(key):
            temp_dict[key].append(i)

        else:
            temp_dict[key] = [i]

    return list(temp_dict.values())
