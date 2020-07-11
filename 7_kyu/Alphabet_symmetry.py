# Kata: Alphabet Symmetry
# https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0

# Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2. 
# In the alphabet, a and b are also in positions 1 and 2. 
# Notice also that d and e in abode occupy the positions they would occupy in the alphabet, 
# which are positions 4 and 5.
# Given an array of words, return an array of the number of letters that 
# occupy their positions in the alphabet for each word. For example,

# solve(["abode","ABc","xyzD"]) = [4, 3, 1]
# See test cases for more examples.

# Input will consist of alphabet characters, both uppercase and lowercase. No spaces.

# Good luck!

# If you like this Kata, please try:
# Last digit symmetry
# Alternate capitalization

def solve(arr):
    result = []
    for s in arr:
        result.append(sum(1 for i, c in enumerate(s.lower()) if ord(c)-97 == i )) 
    return result


print(solve(["abode","ABc","xyzD"]),[4,3,1])
print(solve(["abide","ABc","xyz"]),[4,3,0])
print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]),[6,5,7])
print(solve(["encode","abc","xyzD","ABmD"]),[1, 3, 1, 3])