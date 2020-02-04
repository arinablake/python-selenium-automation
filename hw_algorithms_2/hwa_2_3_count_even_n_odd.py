# Посчитать четные и нечетные цифры числа. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Enter number '))

def count_even_odd(num):
    even_count = 0
    odd_count = 0
    lst = [int(i) for i in str(num)]
    for i in lst:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(str(even_count) + ' even digits and ' + str(odd_count) + ' odd digits')
count_even_odd(num)
