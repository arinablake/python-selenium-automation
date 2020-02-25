# Вводится ненормированная строка, у которой могут быть пробелы в начале, в конце и между словами более одного пробела.
# Привести ее к нормированному виду, т.е. удалить все пробелы в начале и конце, а между словами оставить только один пробел.

'   Enter  some     abnormal string   '


def clean_string(string):
    clean_beg_end = string.strip(' ')
    array = clean_beg_end.split(' ')
    result = []
    for item in array:
        if not item == '':
            result.append(item)
    return ' '.join(result)

print(clean_string('          Enter  some     abnormal                 string   '))