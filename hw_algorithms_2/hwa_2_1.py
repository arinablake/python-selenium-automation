# Sum of 3 modified
#  Домашнее задание: Написать программу для числа из любого количества цифр.
#  Вместо числа из 3 цифр, нужно считать сумму числа из n цифр.
#  Где  n вводит пользователь с клавиатуры. Только положительные.



n = int(input("Enter a number: "))
sum = 0
while(n > 0):
    dig = n % 10
    sum = sum + dig
    n = n // 10
print("The total sum of digits is: ", sum)