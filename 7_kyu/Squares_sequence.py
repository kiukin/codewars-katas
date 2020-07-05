# Kata: Squares sequence
# https://www.codewars.com/kata/5546180ca783b6d2d5000062

# Complete the function that returns an array of length n, 
# starting with the given number x and the squares of the previous number. 
# If n is negative or zero, return an empty array/list.

# Examples
# 2, 5  -->  [2, 4, 16, 256, 65536]
# 3, 3  -->  [3, 9, 81]

def squares(x, n):
    return [x**2**(i) for i in range(n)]