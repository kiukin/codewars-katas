# Kata: Jumping Number (Special Numbers Series #4)
# https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed

# Definition

# Jumping number is the number that All adjacent digits in it differ by 1.

# Task

# Given a number, Find if it is Jumping or not .

# Warm-up (Highly recommended)

# Playing With Numbers Series

# Notes

# Number passed is always Positive .

# Return the result as String .

# The difference between ‘9’ and ‘0’ is not considered as 1 .

# All single digit numbers are considered as Jumping numbers.

# Input >> Output Examples

# jumpingNumber(9) ==> return "Jumping!!"
# Explanation:

# It's single-digit number
# jumpingNumber(79) ==> return "Not!!"
# Explanation:

# Adjacent digits don't differ by 1
# jumpingNumber(23) ==> return "Jumping!!"
# Explanation:

# Adjacent digits differ by 1
# jumpingNumber(556847) ==> return "Not!!"
# Explanation:

# Adjacent digits don't differ by 1
# jumpingNumber(4343456) ==> return "Jumping!!"
# Explanation:

# Adjacent digits differ by 1
# jumpingNumber(89098) ==> return "Not!!"
# Explanation:

# Adjacent digits don't differ by 1
# jumpingNumber(32) ==> return "Jumping!!"
# Explanation:

# Adjacent digits differ by 1

def jumping_number(number):
    num = [int(d) for d in str(number)]
    
    for i,n in enumerate(num[:-1]):
        if abs(n - num[i+1]) != 1:
            return "Not!!"
    return "Jumping!!"


print(jumping_number(1), "Jumping!!")
print(jumping_number(7), "Jumping!!")
print(jumping_number(9), "Jumping!!")
print(jumping_number(23), "Jumping!!")
print(jumping_number(32), "Jumping!!")
print(jumping_number(79), "Not!!")
print(jumping_number(98), "Jumping!!")
print(jumping_number(8987)    , "Jumping!!")
print(jumping_number(4343456) , "Jumping!!")
print(jumping_number(98789876), "Jumping!!")