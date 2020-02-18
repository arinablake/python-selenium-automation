# Посчитайте, сколько раз символ встречается в строке. Строка и символ вводятся с клавиатуры.DON’T USE METHOD COUNT

x = str(input("Enter the symbol: "))
string = str(input("Enter the String: "))

def count_x(string):
    result = 0
    for i in string:
        if x == i:
            result += 1
    return result

print(count_x(string))



