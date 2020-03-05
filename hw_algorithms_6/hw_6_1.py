# Дан лист. Вернуть лист, состоящий из элементов, которые меньше среднего арифметического исходного листа.
# С.а. = сумма элементов разделить на количество.

from random import randint

length = int(input(f'Enter length of array '))
array = []

for i in range(length):
    item = randint(0,100)
    array.append(item)
print(array)
sum = 0
ma = 0
for item in array:
    sum += item
ma = sum / len(array)
print(ma)
new_list = []
for item in array:
    if item < ma:
        new_list.append(item)
print(new_list)

