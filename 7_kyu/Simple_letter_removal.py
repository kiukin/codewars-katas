# Kata: Simple letter removal
# https://www.codewars.com/kata/5b728f801db5cec7320000c7

# In this Kata, you will be given a lower case string and 
# your task will be to remove k characters from that string using the following rule:

# - first remove all letter 'a', followed by letter 'b', then 'c', etc...
# - remove the leftmost character first.

# For example: 
# solve('abracadabra', 1) = 'bracadabra' # remove the leftmost 'a'.
# solve('abracadabra', 2) = 'brcadabra'  # remove 2 'a' from the left.
# solve('abracadabra', 6) = 'rcdbr'      # remove 5 'a', remove 1 'b' 
# solve('abracadabra', 8) = 'rdr'
# solve('abracadabra',50) = ''
# More examples in the test cases. Good luck!

# Please also try:
# Simple time difference
# Simple remove duplicates

def solve(st,k): 
    order = sorted(st)
    for el in order[:k]:
        st = st.replace(el,"",1)
    return st
    

solve('abracadabra', 1) 

