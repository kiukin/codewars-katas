# Kata: Geometry Basics: Triangle Perimeter in 2D
# https://www.codewars.com/kata/58e3e62f20617b6d7700120a

# This series of katas will introduce you to basics of doing geometry with computers.

# Point objects have x, y attributes. 
# Triangle objects have attributes a, b, c describing their corners, each of them is a Point.

# Write a function calculating perimeter of a Triangle defined this way.

# Tests round answers to 6 decimal places.

import math
 
def triangle_perimeter(triangle):
    l1 = get_distance(triangle.a, triangle.b)
    l2 = get_distance(triangle.b, triangle.c)
    l3 = get_distance(triangle.a, triangle.c)
    return sum((l1,l2,l3))
    
def get_distance(p1, p2):
    dist = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2) 
    return dist