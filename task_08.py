#  Task - done

def multiply_numbers(inputs=None) -> int:
    convert = str(inputs)
    result = 1
    for i in range(len(convert)):
        if convert[i].isdigit():
            result *= int(convert[i])

    if result != 1:
        return result


#print(multiply_numbers()) # => None
#print(multiply_numbers('ss')) # => None
#print(multiply_numbers('1234')) # => 24
#print(multiply_numbers('sssdd34')) # => 12
#print(multiply_numbers(2.3)) # => 6
#print(multiply_numbers([5, 6, 4])) # => 120