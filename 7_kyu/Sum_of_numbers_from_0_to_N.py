# Kata: Sum of numbers from 0 to N
# https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763

# Description:

# We want to generate a function that computes the series starting from 0 and ending 
# until the given number.

# Example:

# Input:

# > 6
# Output:

# 0+1+2+3+4+5+6 = 21

# Input:

# > -15
# Output:

# -15<0

# Input:

# > 0
# Output:

# 0=0

def show_sequence(n):
    if n == 0:
        return "0=0"
    elif n < 0:
        return f"{n}<0"
    else:
        seq = [i for i in range(n+1)]
        return f"{'+'.join(map(str, seq))} = {sum(seq)}"