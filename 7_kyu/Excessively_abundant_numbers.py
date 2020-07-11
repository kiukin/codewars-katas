# Kata: Excessively Abundant Numbers
# https://www.codewars.com/kata/56a75b91688b49ad94000015

# An abundant number or excessive number is a number for 
# which the sum of its proper divisors is greater than the number itself.
# The integer 12 is the first abundant number. 
# Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16 (> 12).
# Derive function abundantNumber(num)/abundant_number(num) 
# which returns true/True/.true. if num is abundant, false/False/.false. if not.

def abundant_number(num):
    return sum(i for i in range(1,num) if num%i == 0) > num 

print(abundant_number(12), True)
print(abundant_number(18), True)
print(abundant_number(37), False)
print(abundant_number(120), True)
print(abundant_number(77), False)
print(abundant_number(118), False)
print(abundant_number(5830), True)
print(abundant_number(11410), True)
print(abundant_number(14771), False)
print(abundant_number(11690), True)