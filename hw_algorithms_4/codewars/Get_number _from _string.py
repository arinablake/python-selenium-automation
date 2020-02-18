# Write a function which removes from string all non-digit characters and parse the remaining to number.
# E.g: "hell5o wor6ld" -> 56

def get_number_from_string(string):
    new_string = ''
    for i in string:
        if i.isdigit():
            new_string += i
    return int(new_string)

print(get_number_from_string('N2ew Y3or5k Ci0ty'))