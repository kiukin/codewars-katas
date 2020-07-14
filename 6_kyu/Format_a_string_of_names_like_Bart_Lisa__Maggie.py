# Kata: Format a string of names like 'Bart, Lisa & Maggie
# https://www.codewars.com/kata/53368a47e38700bd8300030d

# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas except for the last two names, 
# which should be separated by an ampersand.

# Example:

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'

# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'

# namelist([])
# # returns ''
# Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.


def namelist(names):
    
    l = len(names)
    result = ""
    
    for i, name in enumerate(names):
        name = name.get('name')
        
        if i == l - 1:
            result += name
        elif i == l -2:
            result += name + " & "
        else:
            result += name + ", "
            
    return result

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge',
"Must work with many names")
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
"Must work with many names")
print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa', 
"Must work with two names")
print(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
print(namelist([]), '', "Must work with no names")

