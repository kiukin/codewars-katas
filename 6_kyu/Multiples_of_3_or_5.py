# Kata: Multiples of 3 or 5
# https://www.codewars.com/kata/514b92a657cdc65150000006

# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 
# below the number passed in.

# Note: If the number is a multiple of both 3 and 5, only count it once.

# Courtesy of ProjectEuler.net

def solution(number):
    num_list = []
    for num in range(0, number):
        if num % 3 == 0 or num % 5 == 0:
            num_list.append(num)
    return sum(num_list)
  