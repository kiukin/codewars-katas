# Nova polynomial add

# This kata is from a series on polynomial handling. ( #1 #2 #3 #4 )

# Consider a polynomial in a list where each element in the list element corresponds to a factor. 
# The factor order is the position in the list. 
# The first element is the zero order factor (the constant).

# p = [a0, a1, a2, a3] signifies the polynomial a0 + a1x + a2x^2 + a3*x^3

# In this kata add two polynomials:
# poly_add ( [1, 2], [1] ) = [2, 2]

# return the sum of the two polynomials p1 and p2.  

from itertools import zip_longest
def poly_add(p1, p2):
    return [x+y for x,y in zip_longest(p1,p2,fillvalue=0)]