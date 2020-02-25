def name_shuffler(str_):
    name = str_.split()
    return ' '.join(name[::-1])

    #return ' '.join(str_.split(' ')[::-1])

print(name_shuffler('Bill Gates'))