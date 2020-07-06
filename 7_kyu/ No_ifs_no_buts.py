# Kata: No ifs no buts
# https://www.codewars.com/kata/592915cc1fad49252f000006

# Write a function that accepts two parameters (a and b) and says whether a is smaller than, 
# bigger than, or equal to b.

# Here is an example code:

# var noIfsNoButs = function (a,b) {
#   if(a > b) return a + " is greater than " + b
#   else if(a < b) return a + " is smaller than " + b
#   else if(a == b) return a + " is equal to " + b
# }
# There's only one problem...

# You can't use if statements, and you can't use shorthands like (a < b)?true:false;

# in fact the word "if" and the character "?" are not allowed in the code.

# Inputs are guarenteed to be numbers

def no_ifs_no_buts(a, b):
    
    result = sorted(set((a,b)))
    
    d = {
        1: "equal to",
        2: "smaller than",
        3: "greater than"
    } 
                    
    return "{} is {} {}".format(a, d[len(result)+result.index(a)] ,b)