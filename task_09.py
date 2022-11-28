#  Task - Done!

def connect_dicts(dict1: dict, dict2: dict):
    template_dict = {}

    if sum(dict1.values()) < sum(dict2.values()) or sum(dict1.values()) == sum(dict2.values()):
        template_merge = (dict1 | dict2)
    else:
        template_merge = (dict2 | dict1)

    for key, value in template_merge.items():
        if value > 10:
            template_dict[key] = value

    return dict(sorted(template_dict.items(), reverse=True))


#print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))  # => { "c": 11, "b": 12 }
#print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))  # => { "d": 11, "c": 12, "a": 13 }
#print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))  # => { "c": 11, "b": 12, "a": 15 }
