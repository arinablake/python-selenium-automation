#Сделать декомпрессию записи “а4б3в2г”

string = "а4б3в2г"
new_str = ""
a = 0

for i in string:
    if i.isalpha():
        new_str += i
        a = i
    if i.isdigit():
        new_str += str((int(i) - 1) * a)

print(new_str)