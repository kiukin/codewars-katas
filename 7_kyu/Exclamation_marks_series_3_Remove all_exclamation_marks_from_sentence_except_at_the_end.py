# Kata: Exclamation marks series #3: Remove all exclamation marks from sentence except at the end
# https://www.codewars.com/kata/57faefc42b531482d5000123


# Description:

# Remove all exclamation marks from sentence except at the end.

# Examples

# remove("Hi!") == "Hi!"
# remove("Hi!!!") == "Hi!!!"
# remove("!Hi") == "Hi"
# remove("!Hi!") == "Hi!"
# remove("Hi! Hi!") == "Hi Hi!"
# remove("Hi") == "Hi"

def remove(s):

    count = len(s) - len(s.rstrip('!'))

    result = s.replace('!','') + '!' * count
    
    return result