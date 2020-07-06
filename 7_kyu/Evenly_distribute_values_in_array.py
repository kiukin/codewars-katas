# Kata: Evenly distribute values in array
# https://www.codewars.com/kata/5bb50eb68f8bbdb4b300021d/train/python

# Your distributeEvenly function will take an array as an argument and needs to
# return a new array with the values distributed evenly.

# Example:
# Argument: ['one', 'one', 'two', 'two', 'three', 'three', 'four', 'four']
# Result: ['one', 'two', 'three', 'four', 'one', 'two', 'three', 'four']

# The underlying order will stay the same as in the original array. So in the case of our argument above,
# one comes before two so it stays this way in the returned array.

# The aim is to have the longest possible chain of evenly distributed values (from the left to right), 
# this means that an argument with many of the same elements might have many 
# which are repeated at the end.

# Example:
# Argument: ['one', 'one', 'one', 'one', 'one', 'two', 'three']
# Result: [ 'one', 'two', 'three', 'one', 'one', 'one', 'one' ]

def distribute_evenly(lst):
    
    order = []
    result = []
    
    for a in lst:
        if a not in order:
            order.append(a)

    while len(lst):
        for n in order:
            if n in lst:
                result.append(lst.pop(lst.index(n)))
    
    return result
            