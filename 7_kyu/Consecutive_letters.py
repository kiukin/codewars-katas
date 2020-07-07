# Kata: Consecutive letters
# https://www.codewars.com/kata/5ce6728c939bf80029988b57

# In this Kata, we will check if a string contains consecutive letters as they appear in the English alphabet and if each letter occurs only once.

# For example: 
# solve("abc") = True, because it contains a,b,c
# solve("abd") = False, because a, b, d are not consecutive, and c is missing.
# solve("dabc") = True, because it contains a, b, c, d
# solve("abbc") = False, because b does not occur once.
# solve("v") = True
# All inputs will be lowercase letters.

# More examples in test cases. Good luck!


import string
def solve(st):
    return "".join(sorted(st)) in string.ascii_lowercase