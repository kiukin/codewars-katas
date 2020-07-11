# Kata: Reverse words
# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4

# Complete the function that accepts a string parameter, 
# and reverses each word in the string. 
# All spaces in the string should be retained.

# Examples

# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    mask = "".join("*" if w != " " else w for w in text)
    r = list("".join(word[::-1] for word in text.split()))
    result = ""
    for i in mask:
        if i == "*":
            result += r.pop(0)
        else:
            result += i
    return result

# Alternative solution
# return ' '.join(s[::-1] for s in str.split(' '))