# В строке найти и заменить одну подстроку на другую. Если одинаковых подстрок несколько, заменить все.
# Строка, значение которое надо заменить и значение, на которое надо заменить вводятся с клавиатуры.
# DON’T USE METHOD REPLACE

tb_repl = str(input("Enter the str to be replaced: "))
repl = str(input("Enter the replacement: "))
string = str(input("Enter the String: "))


string = list(string)
result = []
for i in string:
    if i == tb_repl:
        i = repl
        result.append(i)
    else:
        result.append(i)

print(''.join(result))


# tb_repl = str(input("Enter the str to be replaced: "))
# repl = str(input("Enter the replacement: "))
# string = str(input("Enter the String: "))
#
#
# string = string.split(' ')
# result = []
# for i in string:
#     if i == tb_repl:
#         i = repl
#         result.append(i)
#     else:
#         result.append(i)
#
# print(' '.join(result))

# подстрока здесь значит символ или слово?

# def replacement(string):
#     # result = ''
#     for i in string:
#         if i == tb_repl:
#             i = repl
#             # result += i
#             return i
# print(replacement(string))
#