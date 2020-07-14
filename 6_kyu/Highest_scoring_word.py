# Kata: Highest Scoring Word
# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272

# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet:
# a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

def high(x):
    
    result = []
    for word in x.split():

        score = sum(ord(c)-96 for c in word) 
        result.append((score, word))
    
    return max(result)[1]

print(high('man i need a taxi up to ubud'), 'taxi')
print(high('what time are we climbing up the volcano'), 'volcano')
print(high('take me to semynak'), 'semynak')