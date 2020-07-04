# Kata: Shortest Word
# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    word_len = (len(w) for w in s.split())
    return min(word_len)


# More elegant solution:
# len(min(s.split(' '), key=len))