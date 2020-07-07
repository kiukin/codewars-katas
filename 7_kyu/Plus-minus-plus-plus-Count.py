# Kata: Plus - minus - plus - plus - ... - Count
# https://www.codewars.com/kata/5bbb8887484fcd36fb0020ca

# Count how often sign changes in array.

# result
# number from 0 to ... . Empty array returns 0

# example
# const arr = [1, -3, -4, 0, 5];

# /*
# | elem | count |
# |------|-------|
# |  1   |  0    |
# | -3   |  1    |
# | -4   |  1    |
# |  0   |  2    |
# |  5   |  2    |
# */
# catchSignChange(arr) == 2;

def catch_sign_change(lst):
    lst = ["pos" if el >= 0 else "neg" for el in lst]
    result = 0
    for i in range (1, len(lst)):
        if lst[i] != lst[i-1]:
            result += 1
    return result