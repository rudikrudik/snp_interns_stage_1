def multiply_numbers(inputs=None) -> int:
    convert = str(inputs)
    result = 1
    for i in range(len(convert)):
        if convert[i].isdigit():
            result *= int(convert[i])

    if result != 1:
        return result
