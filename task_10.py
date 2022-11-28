import string


def count_words(string_word: str) -> dict:
    result = {}

    for punctuation in string.punctuation:
        if punctuation in string_word:
            string_word = string_word.replace(punctuation, '')

    string_split = string_word.lower().split()

    for i in string_split:
        if result.get(i, None):
            result[i] += 1
        else:
            result[i] = 1

    return result
