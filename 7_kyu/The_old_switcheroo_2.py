# Kata: The old switcheroo 2
# https://www.codewars.com/kata/55d6a0e4ededb894be000005

# This is a follow up from my kata The old switcheroo</br/>

# Write

# def encode(str)
# that takes in a string str and 
# replaces all the letters with their respective positions in the English alphabet.

# encode('abc') == '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
# encode('codewars') == '315452311819'
# encode('abc-#@5') == '123-#@5'
# String are case sensitive.

import string
def encode(str_):
    return "".join((str(ord(n)-96) if n in string.ascii_lowercase else n for n in str_.lower())) 

