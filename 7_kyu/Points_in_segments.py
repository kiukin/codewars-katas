# Kata: Points in Segments
# https://www.codewars.com/kata/5baa25f3246d071df90002b7

# You are given a set of n segments on the axis Ox, 
# each segment has integer endpoints between 0 and m inclusive.
# Segments may intersect, overlap or even coincide with each other. 
# Each segment is characterized by two integers li and ri — coordinates of the left 
# and of the right endpoints.

# Consider all integer points between 0 and m inclusive. 
# Your task is to print all such points that don't belong to any segment. 
# The point x belongs to the segment [l;r] if and only if l ≤ x ≤ r.

# Input:
#  m — the upper bound for coordinates;
#  array of coordinates li and ri 0 ≤ li ≤ ri ≤ m — the endpoints of the i-th segment.
#  Segments may intersect, overlap or even coincide with each other.

# Output:
#  All points from 0 to m that don't belong to any segment.

# Examples:

# segments(5, [(2,2),(1,2),(5,5)]) => [0,3,4]
# segments(7, [(0,7)]) => []

def segments(m, a):
    segments = set(j for start,end in a for j in range(start, end+1))
    result = [i for i in range (m+1) if i not in segments]
    return result

print(segments(5, [(2, 2), (1, 2), (5, 5)]), [0, 3, 4])
print(segments(7, [(0, 7)]), [])


# Alternative solution
# return [i for i in range(m+1) if not any(a<=i<=b for a,b in arr)]