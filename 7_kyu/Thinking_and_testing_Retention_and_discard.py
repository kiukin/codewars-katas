# Kata: Thinking & Testing : Retention and discard
# https://www.codewars.com/kata/56ee0448588cbb60740013b9

# No Story

# No Description

# Only by Thinking and Testing

# Look at the results of the testcases, and guess the code!

def mystery(n):
    return [i for i in range(1, n+1, 2) if n%i == 0]    


print(mystery(-1), [])
print(mystery(0), [])
print(mystery(1), [1])
print(mystery(2), [1])
print(mystery(3), [1,3])
print(mystery(4), [1])
print(mystery(5), [1, 5])
print(mystery(6), [1, 3])
print(mystery(7), [1, 7])
print(mystery(8), [1])
print(mystery(9), [1, 3, 9])
print(mystery(10), [1, 5])