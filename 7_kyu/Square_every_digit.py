# Square Every Digit
# https://www.codewars.com/kata/546e2562b03326a88e000020

# Welcome. In this kata, you are asked to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out, 
# because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    # Convert int to string, using list comprehension to pick each digit 
    # and then convert to an int list 
    digit = [int(d) for d in str(num)]
    
    # Square all digit in the digit list and combine them back to a string
    result =  "".join(str(d**2) for d in digit )
    
    # Convert string to int and return
    return int(result)

print(square_digits(1234))

    