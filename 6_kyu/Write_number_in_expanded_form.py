# Kata: Write Number in Expanded Form
# https://www.codewars.com/kata/5842df8ccbd22792a4000245

# Write Number in Expanded Form

# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

# If you liked this kata, check out part 2!!

def expanded_form(num):
    num = str(num)
    l = len(num)

    result = []
    for i,d in enumerate(num,1):
        if d != '0': 
            result.append(d + "0"*(l-i))
            
    return " + ".join(result)



print(expanded_form(12), '10 + 2')
print(expanded_form(42), '40 + 2')
print(expanded_form(70304), '70000 + 300 + 4')