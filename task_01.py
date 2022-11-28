#  Task - Done!

def is_palindrome(target_str: str) -> bool:
    temp_str = []

    try:
        convert_to_srt = str(target_str)
    except ValueError:
        return False

    for i in range(len(convert_to_srt)):
        if convert_to_srt[i] in "-+/, :;!'`~":
            continue
        else:
            temp_str.append(convert_to_srt[i].lower())

    if temp_str == temp_str[::-1]:
        return True
    else:
        return False

