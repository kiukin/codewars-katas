# Kata: Filter unused digits
# https://www.codewars.com/kata/55de6173a8fbe814ee000061

# Given few numbers, you need to print out the digits that are not being used.

# Example:

# unused_digits(12, 34, 56, 78) # "09"
# unused_digits(2015, 8, 26) # "3479"

# Note:
# Result string should be sorted
# The test case won't pass Integer with leading zero

def unused_digits(*args):
    def unused_digits(*args):
    result = ""
    for n in "0123456789":
        if n not in str(args):
            result += n
    return result
    
# Alternative elegant solution
# return "".join(number for number in "0123456789" if number not in str(args))