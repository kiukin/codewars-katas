# Kata: Encrypt this!
# https://www.codewars.com/kata/5848565e273af816fb000449

# Acknowledgments:

# I thank yvonne-liu for the idea and for the example tests :)

# Description:

# Encrypt this!

# You want to create secret messages which can be deciphered by the Decipher this! kata. 
# Here are the conditions:

# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter needs to be converted to its ASCII code.
# The second letter needs to be switched with the last letter
# Keepin' it simple: There are no special characters in input.
# Examples:

# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"

def encrypt_this(text):
    result = []
    
    # turn text into list
    words = text.split()
    
    # iterate the word
    for word in words:
        
        word = list(word)
    
        # turn first letter to Ascii code using ord()
        word[0] = str(ord(word[0]))
        
        # if word len > 2:
        if len(word) >= 2:
        
            # switch 2nd and last letter
            word[1], word[-1] = word[-1], word[1]
        
    
        # join back the words and append to reults
        result.append("".join(word))
    
    # return joined results
    return " ".join(result)

print("", "")
print(encrypt_this("A wise old owl lived in an oak"), "65 119esi 111dl 111lw 108dvei 105n 97n 111ka")
print(encrypt_this("The more he saw the less he spoke"), "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp")
print(encrypt_this("The less he spoke the more he heard"), "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare")
print(encrypt_this("Why can we not all be like that wise old bird"), "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri")
print(encrypt_this("Thank you Piotr for all your help"), "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple")
