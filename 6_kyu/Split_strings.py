# Kata: Split Strings
# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing 
# second character of the final pair with an underscore ('_').

# Examples:

# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(s):

    l = len(s)
    if l % 2 == 1:
        s += '_'
    
    result = []
    
    for i in range(0,l,2):
        result.append(s[i:i+2])
    
    return result

print(solution("asdfadsf"), ['as', 'df', 'ad', 'sf'])
print(solution("asdfads"), ['as', 'df', 'ad', 's_'])
print(solution(""),[])
print(solution("x"),["x_"])



