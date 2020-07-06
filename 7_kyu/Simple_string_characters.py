# Kata: Simple string characters
# https://www.codewars.com/kata/5a29a0898f27f2d9c9000058

# In this Kata, you will be given a string and your task will be to 
# return a list of ints detailing the count of uppercase letters, lowercase, 
# numbers and special characters, as follows.

# solve("*'&ABCDabcde12345") = [4,5,5,3]. 
# --the order is: uppercase letters, lowercase, numbers and special characters.
# More examples in the test cases.

# Good luck!

# Please also try Simple remove duplicates


def solve(s):
    res= [0,0,0,0]
    for c in s:
        if c.isupper():
            res[0] += 1
        elif c.islower():
            res[1] += 1
        elif c.isdigit():
            res[2] += 1
        else:
            res[3] += 1
    return res