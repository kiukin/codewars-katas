# Kata: No oddities here

# Write a small function that returns the values of an array that are not odd.

# All values in the array will be integers. Return the good values in the order they are given.

# def no_odds(values):

def no_odds(values): 
    return [v for v in values if v%2 == 0]