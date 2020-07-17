# Kata: max diff - easy
# https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095

# You must implement a function maxDiff that return the difference between the biggest and the smallest value in a list(lst) received as parameter.

# The list(lst) contains integers, that means it may contain some negative numbers.

# If the list is empty or contains a single element, return 0.

# The list(lst) is not sorted.

# maxDiff([1, 2, 3, 4]); //return 3, because 4 - 1 == 3
# maxDiff([1, 2, 3, -4]); //return 7, because 3 - (-4) == 7
# Have fun!

def max_diff(lst):
    if not len(lst) : return 0
    lst.sort()
    return lst[-1] - lst[0]

# def max_diff(lst):
#     return 0 if not lst else max(lst) - min(lst)

print(max_diff([0, 1, 2, 3, 4, 5, 6]), 6)
print(max_diff([-0, 1, 2, -3, 4, 5, -6]), 11)
print(max_diff([0, 1, 2, 3, 4, 5, 16]), 16)
print(max_diff([16]), 0)
print(max_diff([]), 0)
