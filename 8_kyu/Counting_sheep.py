# Kata: Counting sheep
# https://www.codewars.com/kata/54edbc7200b811e956000556


# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

# For example,

# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]

# The correct answer would be 17.

# Hint: Don't forget to check for bad values like null/undefined


def count_sheeps(sheep):
    return sheep.count(True)


array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ];
              
print(count_sheeps(array1), 17, "There are 17 sheeps in total, not %s" % count_sheeps(array1))