def division(n1,n2):
    result = 0
    if n2 == 0:
        print("You can't divide on 0")
    while n1 >= n2:
        n1 = n1 - n2
        result += 1
    return result

print(division(30, 6))