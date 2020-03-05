# Найти максимальный элемент среди минимальных элементов строк матрицы.

def max_num_matrix(matrix):
    min_list = []
    for item in matrix:
        for num in item:
            min = item[0]
            index = 0
            while index < len(item):
                if item[index] < min:
                    min = item[index]
                index += 1
        print(min)
        min_list.append(min)
    print(min_list)

    max_min = min_list[0]
    index = 0
    for i in min_list:
        while index < len(min_list):
            if min_list[index] > max_min:
                max_min = min_list[index]
            index += 1
    return max_min


print(max_num_matrix([[2, 4, 6], [10, 20, 30], [23, 14, 65]]))