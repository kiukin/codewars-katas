# Kata: Minimum to multiple
# https://www.codewars.com/kata/5e030f77cec18900322c535d/solutions/python

# Given two integers a and x, return the minimum non-negative number to add to / subtract 
# from a to make it a multiple of x.

# minimum(10, 6)  #= 2
# 10+2 = 12 which is a multiple of 6
# Note

# 0 is always a multiple of x
# Constraints
# 1 <= a <= 106
# 1 <= x <= 105

import math
def minimum(a, x):
    poss1 = a%x
    poss2 = math.ceil(a/x)*x - a
    return min(poss1, poss2)


# Alternative solution:
# return min(a % x, -a % x)