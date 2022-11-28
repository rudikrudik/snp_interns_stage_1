#  Task - Done!

def combine_anagrams(target_list: list) -> list:
    temp_list = []
    temp_word = []

    for i in target_list:
        if len(temp_word) == 0:
            temp_word.append(i)
        else:
            for j in target_list:
                if temp_word[-1] != j and sorted(temp_word[-1]) == sorted(j):
                    temp_word.append(target_list.pop(target_list.index(j)))

            else:
                temp_list.append(temp_word)
                temp_word = []
                temp_word.append(i)

    return temp_list
