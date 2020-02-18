# Complete the solution so that it reverses all of the words within the string passed in.
#
# Example:
# reverseWords("hello world!"), "world! hello")

def reverseWords(str):
    list = str.split()
    a = list[::-1]
    b = ""
    for i in a:
        b = b + i + " "
    return b.strip(" ")

print(reverseWords("Hold my beer!"))



# def reverseWords(str):
#     return " ".join(str.split(" ")[::-1])