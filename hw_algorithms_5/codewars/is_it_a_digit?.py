#Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.


def is_digit(n):
    if n.isdigit() and len(n) == 1:
        return True
    else:
        return False

print(is_digit('a'))
print(is_digit('3'))