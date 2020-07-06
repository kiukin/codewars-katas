# Kata: Counting Array Elements
# https://www.codewars.com/kata/5569b10074fe4a6715000054

# Write a function that takes an array and counts the number of each unique element present.
# count(['james', 'james', 'john']) 
# #=> { 'james' => 2, 'john' => 1}

from collections import Counter
def count(array):
    return Counter(array)