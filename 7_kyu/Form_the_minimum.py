# Kata: Form The Minimum
# https://www.codewars.com/kata/5ac6932b2f317b96980000ca

# Task

# Given a list of digits, return the smallest number that could be formed from these digits, using the digits only once (ignore duplicates).

# Notes:

# Only positive integers will be passed to the function (> 0 ), no negatives or zeros.
# Input >> Output Examples

# minValue ({1, 3, 1})  ==> return (13)
# Explanation:

# (13) is the minimum number could be formed from {1, 3, 1} , Without duplications

# minValue({5, 7, 5, 9, 7})  ==> return (579)
# Explanation:

# (579) is the minimum number could be formed from {5, 7, 5, 9, 7} , Without duplications

# minValue({1, 9, 3, 1, 7, 4, 6, 6, 7}) return  ==> (134679)
# Explanation:

# (134679) is the minimum number could be formed from {1, 9, 3, 1, 7, 4, 6, 6, 7} , Without duplications


def min_value(digits):
    digs_set = list(set(digits))
    digs_set.sort()
    result = "".join(map(str, digs_set))
    return int(result)


print(min_value([1, 3, 1]), 13)
print(min_value([4, 7, 5, 7]), 457)
print(min_value([4, 8, 1, 4]), 148)