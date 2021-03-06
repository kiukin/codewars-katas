# Kata: Most valuable character
# https://www.codewars.com/kata/5dd5128f16eced000e4c42ba

# In this Kata, you will be given a string and your task is to return the most valuable character. The value of a character is the difference between the index of its last occurrence and the index of its first occurrence. Return the character that has the highest value. If there is a tie, return the lexicographically lowest character.

# All inputs will be lower case.

# For example:
# solve('a') = 'a'
# solve('ab') = 'a'. Last occurrence is equal to first occurrence of each character. Return lexicographically lowest.
# solve("axyzxyz") = 'x'
# More examples in test cases. Good luck!

def solve(st):
    d = { a: st.rfind(a) - st.find(a) for a in sorted(set(st)) }    
    return max(d, key=lambda x: d[x])


# Alternative elegant solution
# return min(set(st), key=lambda c: (st.index(c)-st.rindex(c), c))
