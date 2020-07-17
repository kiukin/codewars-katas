# Kata: Consecutive string  
# https://www.codewars.com/kata/56a5d994ac971f1ac500003e


# You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

# Example:

# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

# Note

# consecutive strings : follow one after another without an interruption

def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0: return ""
    
    for i in range(n):
        strarr[i] = "".join(strarr[i:i+k])
        
    return max(strarr, key=len)

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
print(longest_consec([], 3), "")
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
        