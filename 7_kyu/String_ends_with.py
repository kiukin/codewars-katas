# Kata: String ends with?
# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d

# Complete the solution so that it returns true if the first argument(string) passed in 
# ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(string, ending):
    endingLen = len(ending)
    return True if ending == "" else string[-endingLen:] == ending

print(solution('abcde', 'cde'), True)
print(solution('abcde', 'abc'), False)
print(solution('abcde', ''), True)


# Built in function:
# return string.endswith(ending)