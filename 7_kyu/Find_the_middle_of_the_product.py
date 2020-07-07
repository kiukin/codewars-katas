# Kata: Find the Middle of the Product
# https://www.codewars.com/kata/5ac54bcbb925d9b437000001

# Given a string of characters, I want the function findMiddle()/find_middle() to return 
# the middle number in the product of each digit in the string.

# Example: 's7d8jd9' -> 7, 8, 9 -> 7*8*9=504, thus 0 should be returned as an integer.

# Not all strings will contain digits. In this case and the case for any non-strings, return -1.

# If the product has an even number of digits, return the middle two digits

# Example: 1563 -> 56

# NOTE: Remove leading zeros if product is even and the first digit of the two is a zero. 
# Example 2016 -> 1

def find_middle(string):
    if type(string) != str: return -1
    digits = "".join(c for c in string if c.isdigit())
    if digits == "": return -1
    
    prod = 1 
    for d in (map(int, digits)):
        prod = prod * d
    
    l = len(str(prod))
    
    if l%2 == 0 and l != 0:
        return int(str(prod)[l//2-1:l//2+1])
    else:
        return int(str(prod)[l//2])
    return 0