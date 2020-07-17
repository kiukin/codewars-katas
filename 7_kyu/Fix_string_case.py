# Kata: Fix string case
# https://www.codewars.com/kata/5b180e9fedaa564a7000009a

# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and 
# your task is to convert that string to either lowercase only or uppercase only based on:

# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
# For example:

# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
# More examples in test cases. Good luck!


def solve(s):
    low, up = 0, 0  
    for c in s:
        if c.islower(): low += 1
        elif c.isupper(): up += 1

    if low == up or low > up:
        return s.lower()
    else:
        return s.upper()


print(solve("code"),"code")
print(solve("CODe"),"CODE")
print(solve("COde"),"code")
print(solve("Code"),"code")