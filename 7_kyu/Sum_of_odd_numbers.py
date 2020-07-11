# Kata: Sum of odd numbers
# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064

# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8


import math
def row_sum_odd_numbers(n):
    ending = n - 1 + n**2
    ending_prev = n -2 + (n - 1)**2
    return math.ceil(ending/2)**2 -  math.ceil(ending_prev/2)**2

print(row_sum_odd_numbers(1), 1)
print(row_sum_odd_numbers(2), 8)
print(row_sum_odd_numbers(13), 2197)
print(row_sum_odd_numbers(19), 6859)
print(row_sum_odd_numbers(41), 68921)

# Alternative solution
# return n ** 3
