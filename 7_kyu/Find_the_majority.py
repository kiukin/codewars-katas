# Kata: Find the majority
# https://www.codewars.com/kata/5af974846bf32304a2000e98


# Goal
# Given a list of elements [a1, a2, ..., an], 
# with each ai being a string, write a function **majority** 
# that returns the value that appears the most in the list.
# If there's no winner, the function should return 
# None, NULL, nil, etc, based on the programming language.

# Example
# majority(["A", "B", "A"]) returns "A" majority(["A", "B", "B", "A"]) returns None

from collections import Counter
def majority(arr):
    if not len(arr): return None
    
    m = max(Counter(arr).items(),key=lambda x: x[1])[1]
    
    result = []
    
    for i in arr:
        if arr.count(i) == m:
            result.append(i)
    
    return result[0] if len(set(result)) == 1 else None
    

print(majority(["A", "B", "A"]), "A")
print(majority(["A", "B", "C"]), None)
print(majority(["A", "B", "B", "A"]), None)
print(majority(['A','A','A','A']), "A")
print(majority(['A',]), "A")
print(majority(['A','A','A','BBBBBBBB']), "A")
print(majority(["A", "B", "C", "C"]), "C")
print(majority([]), None)

