def combine_anagrams(target_list: list) -> list:
    temp_dict = {}

    for i in target_list:
        if not temp_dict.get(''.join(sorted(i))):
            temp_dict[''.join(sorted(i))] = [i]
        else:
            temp_dict[''.join(sorted(i))].append(i)

    return list(temp_dict.values())