# Kata: Comfortable words
# https://www.codewars.com/kata/56684677dc75e3de2500002b

# A comfortable word is a word which you can type always alternating the hand you type with 
# (assuming you type using a QWERTY keyboard and use fingers as shown in the image below).

# That being said, create a function which receives a word and returns true/True 
# if it's a comfortable word and false/False otherwise.

# The word will always be a string consisting of only ascii letters from a to z.



# To avoid problems with image availability, here's the lists of letters for each hand:

# Left: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
# Right: y, u, i, o, p, h, j, k, l, n, m


def comfortable_word(word):
    Left = 'qwertasdfgzxcvb'
    Right ='yuiophjklnm'
    
    if word[0] in Left:
        return all( w in Left for w in word[0::2]) and  all( w in Right for w in word[1::2])
    return all( w in Right for w in word[0::2]) and  all( w in Left for w in word[1::2])