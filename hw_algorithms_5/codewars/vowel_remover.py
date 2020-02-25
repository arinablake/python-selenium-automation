# Create a function called shortcut to remove all the lowercase vowels in a given string.
#
# Examples
#
# shortcut("codewars") # --> cdwrs
# shortcut("goodbye")  # --> gdby
# Don't worry about uppercase vowels.
#
#

def shortcut( s ):
    new_string = ""
    vowels = "aeiou"
    for char in s:
        if char not in vowels:
            new_string += char
    return new_string

print(shortcut("Summer"))