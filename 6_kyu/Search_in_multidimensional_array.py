# Kata: search in multidimensional array
# https://www.codewars.com/kata/52840d2b27e9c932ff0016ae

# Write a function that gets a sequence and value and returns true/false 
# depending on whether the variable exists in a multidimentional sequence.
# Example:

# locate(['a','b',['c','d',['e']]],'e'); // should return true
# locate(['a','b',['c','d',['e']]],'a'); // should return true
# locate(['a','b',['c','d',['e']]],'f'); // should return false

def locate(seq, value):
    while any(map(lambda x: isinstance(x, list),seq)):
        new_seq = []
        for el in seq:
            if isinstance(el, list):
                for e in el:
                    new_seq.append(e)
            else:
                new_seq.append(el)
        seq = new_seq
    return value in seq


# Recursive Function:
# def locate(seq, value): 
#     for s in seq:
#         if s == value or (isinstance(s,list) and locate(s, value)): 
#             return True
#     return False

# Yield the flattened array:
# --------------------------------
# def locate(seq, value): 
#     return value in flatten(seq)


# def flatten(seq):
#     for e in seq:
#         if isinstance(e, list):
#             yield from flatten(e)
#         yield e

