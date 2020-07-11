# Kata: Positive to negative binary numbers
# https://www.codewars.com/kata/5becace7063291bebf0001d5

# Given an array of one's and zero's that represents a positive binary number 
# convert the number to two's complement value.

# Two's complement is the way most computers represent positive or negative integers. 
# The most significant bit is negative.

# Examples:

# -8 4 2 1

# [1,1,1,1] = -1

# [1,0,0,0] = -8

# [1,1,0,1] = -3

# To get the two's complement negative notation of an integer, you take the number in binary.

# You then invert the digits, and add one to the result.

# For example:

# [0,0,1,0] = 2 in base 10

# [1,1,0,1] <- Flip the bits

# Add 1

# [1,1,1,0] = -2

# However, the arrays can have varying lengths, not just limited to 4.

def positive_to_negative(binary):
    flip = [ abs(i-1) for i in binary ]
    for i in range(len(binary)-1, -1, -1):
        if flip[i]:
            flip[i] = 0
        else: 
            flip[i] = 1
            break
    return flip