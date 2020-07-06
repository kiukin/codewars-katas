# Kata: SevenAte9
# https://www.codewars.com/kata/559f44187fa851efad000087

# Write a function that removes every lone 9 that is inbetween 7s.

# seven_ate9('79712312') => '7712312'
# seven_ate9('79797') => '777'
# Input: String Output: String

def seven_ate9(str_):
    while "797" in str_:
        str_ = str_.replace("797","77")
    return str_