# Kata: Find the next perfect square!
# https://www.codewars.com/kata/56269eb78ad2e4ced1000013

# You might know some pretty large perfect squares. But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square after 
# the one passed as a parameter. Recall that an integral perfect square is an integer n 
# such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square then -1 should be returned. 
# You may assume the parameter is positive.

# Examples:

# findNextSquare(121) --> returns 144
# findNextSquare(625) --> returns 676
# findNextSquare(114) --> returns -1 since 114 is not a perfect

from math import sqrt 
def find_next_square(sq):
    return -1 if sqrt(sq)%1 != 0 else (sqrt(sq) + 1)**2

