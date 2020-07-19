# Kata: Find the divisors!
# https://www.codewars.com/kata/544aed4c4a30184e960010f4

# Create a function named divisors/Divisors that takes an integer n > 1 
# and returns an array with all of the integer's divisors(except for 1 and the number itself), 
# from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) 
# (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

# Example:

# divisors(12); #should return [2,3,4,6]
# divisors(25); #should return [5]
# divisors(13); #should return "13 is prime"

import math 
def divisors(integer):
    results = set()
    for i in range(2, math.ceil(math.sqrt(integer))+1):
        div, mod = divmod(integer, i)
        if mod == 0:
            results.add(i)
            results.add(div)
        
    return sorted(results) or f"{integer} is prime"

print(divisors(15), [3, 5])
print(divisors(12), [2, 3, 4, 6])
print(divisors(13), "13 is prime")