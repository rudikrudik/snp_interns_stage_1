#  Task - Done!
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

#  print(count_words("A, man, a plan, a canal -- Panama")) # => {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}
#  print(count_words("Doo bee doo bee doo")) # => {"doo": 3, "bee": 2}
