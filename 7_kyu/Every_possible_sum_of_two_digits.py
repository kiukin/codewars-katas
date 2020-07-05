# Kata: Every possible sum of two digits
# https://www.codewars.com/kata/5b4e474305f04bea11000148

# Given a long number, return all the possible sum of two digits of it.

# For example, 12345: all possible sum of two digits from that number are:
# [ 1 + 2, 1 + 3, 1 + 4, 1 + 5, 2 + 3, 2 + 4, 2 + 5, 3 + 4, 3 + 5, 4 + 5 ]

# Therefore the result must be:
# [ 3, 4, 5, 6, 5, 6, 7, 7, 8, 9 ]

def digits(num):
    nums = [int(a) for a in str(num)]
    sums = []
    
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            sums.append(nums[i]+nums[j])
    
    return sums