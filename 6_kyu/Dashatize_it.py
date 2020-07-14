# Kata: Dashatize it
# https://www.codewars.com/kata/58223370aef9fc03fd000071

# Given a number, return a string with dash'-'marks before and after each odd integer, 
# but do not begin or end the string with a dash mark.

# Ex:

# dashatize(274) -> '2-7-4'
# dashatize(6815) -> '68-1-5'

def dashatize(num):
    # None check
    if num == None: 
        return "None"
    
    digits = [digit for digit in str(num)]
    result = ""

    for item in digits:
        if item in '13579':
            result += f"-{item}-"
        else:
            result += item
    
    return result.replace('--','-').strip('-')
    

# 'Basic'
print(dashatize(274),"2-7-4", "Should return 2-7-4")
print(dashatize(5311),"5-3-1-1", "Should return 5-3-1-1")
print(dashatize(86320),"86-3-20", "Should return 86-3-20")
print(dashatize(974302),"9-7-4-3-02", "Should return 9-7-4-3-02")
# 'Weird'
print(dashatize(None),"None", "Should return None")
print(dashatize(0),"0", "Should return 0")
print(dashatize(-1),"1", "Should return 1")
print(dashatize(-28369),"28-3-6-9", "Should return 28-3-6-9")