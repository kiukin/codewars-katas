# Kata: Fake Binary
# https://www.codewars.com/kata/57eae65a4321032ce000002d

# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. 
# Return the resulting string.

def fake_bin(x):
    return "".join("1" if int(c) >= 5 else "0" for c in x)

tests = [
    ["01011110001100111", "45385593107843568"],
    ["101000111101101", "509321967506747"],
    ["011011110000101010000011011", "366058562030849490134388085"],
    ["01111100", "15889923"],
    ["100111001111", "800857237867"],
]

for exp, inp in tests:
    print(fake_bin(inp), exp)