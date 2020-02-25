# В строке, состоящей из слов, разделенных пробелом, найти самое длинное слово.
# Строка вводится с клавиатуры.

'Get More This Season. Shop New Spring Arrivals From Abercrombie'

def long_word(string):
    array = string.split()
    longest_word = 0
    for i in range(1, len(array)):
        if len(array[longest_word]) < len(array[i]):
            longest_word = i
    return array[longest_word]


print(long_word('Get More This Season. Shop New Spring Arrivals From Abercrombie'))