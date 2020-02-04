#Найти максимальное число из трех. Вводятся три целых числа. Определить какое из них наибольшее.

num1 = int(input('Enter 1st number '))
num2 = int(input('Enter 2nd number '))
num3 = int(input('Enter 3rd number '))

def max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print('Max number is 1st number ' + str(num1))
    elif num2 > num1 and num2 > num3:
        print('Max number is 2nd number ' + str(num2))
    elif num1 == num2:
        print('1st number ' + str(num1) + ' is equal to 2nd number ' + str(num2))
    elif num2 == num3:
        print('2nd number ' + str(num2) + ' is equal to 3rd number ' + str(num3))
    elif num1 == num3:
        print('1st number ' + str(num1) + ' is equal to 3rd number ' + str(num3))
    else:
        print('Max number is 3rd number ' + str(num3))

max_number(num1, num2, num3)