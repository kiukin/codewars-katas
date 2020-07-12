# Kata: Hex Word Sum
# https://www.codewars.com/kata/5c46ea433dd41b19af1ca3b3

# Description

# As hex values can include letters A through to F, certain English words can be spelled out, 
# such as CAFE, BEEF, or FACADE. This vocabulary can be extended by using numbers to represent 
# other letters, such as 5EAF00D, or DEC0DE5.

# Given a string, your task is to return the decimal sum of all words in the string 
# that can be interpreted as such hex values.

# Example

# Working with the string BAG OF BEES:

# BAG ==> 0 as it is not a valid hex value
# OF ==> 0F ==> 15
# BEES ==> BEE5 ==> 48869
# So hex_word_sum('BAG OF BEES') returns the sum of these, 48884.

# Notes

# Inputs are all uppercase and contain no punctuation
# 0 can be substituted for O
# 5 can be substituted for S


def hex_word_sum(string):
    sum = 0
    for w in string.split():
        try:
            w = w.replace('O','0').replace('S','5')
            sum += int(w,16)
        except ValueError:
            pass
    return sum      

print(hex_word_sum('DEFACE'), 14613198, 'Should convert hex to decimal correctly') 
print(hex_word_sum('SAFE'), 23294, 'Should be able to interpret "S" as "5"')
print(hex_word_sum('CODE'), 49374, 'Should be able to interpret "O" as "0"')
print(hex_word_sum('BUGS'), 0, 'A word that cannot be converted to hex has value of 0')
print(hex_word_sum(''), 0, 'Empty string returns 0')
print(hex_word_sum('DO YOU SEE THAT BEE DRINKING DECAF COFFEE'), 13565769, 'Should work with multiple words')
print(hex_word_sum('ASSESS ANY BAD CODE AND TRY AGAIN'), 10889952, 'Should work with multiple words')

