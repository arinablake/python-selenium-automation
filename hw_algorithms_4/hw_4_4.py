# Возведение в степень с помощью рекурсии

base_num = int(input("Enter base: "))
exp_num = int(input("Enter exponential value: "))


def power(base_num, exp_num):
    if base_num <= 1:
        return base_num
    elif exp_num == 1:
        return base_num
    elif exp_num != 1:
        return base_num * power(base_num, exp_num - 1)

print("Result:", power(base_num, exp_num))
