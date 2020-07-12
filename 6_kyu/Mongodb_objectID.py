# Kata: Mongodb ObjectID
# https://www.codewars.com/kata/52fefe6cb0091856db00030e

# MongoDB is a noSQL database which uses the concept of a document, rather than a table as in SQL. Its popularity is growing.

# As in any database, you can create, read, update, and delete elements. But in constrast to SQL, when you create an element, a new field _id is created. This field is unique and contains some information about the time the element was created, id of the process that created it, and so on. More information can be found in the MongoDB documentation (which you have to read in order to implement this Kata).

# So let us implement the following helper which will have 2 methods:

# one which verifies that the string is a valid Mongo ID string, and
# one which finds the timestamp from a MongoID string
# Note:

# If you take a close look at a Codewars URL, you will notice each kata's id (the XXX in http://www.codewars.com/dojo/katas/XXX/train/javascript) is really similar to MongoDB's ids, which brings us to the conjecture that this is the database powering Codewars.

# Examples

# The verification method will return true if an element provided is a valid Mongo string and false otherwise:

# Mongo.is_valid('507f1f77bcf86cd799439011')  # True
# Mongo.is_valid('507f1f77bcf86cz799439011')  # False
# Mongo.is_valid('507f1f77bcf86cd79943901')   # False
# Mongo.is_valid('111111111111111111111111')  # True
# Mongo.is_valid(111111111111111111111111)    # False
# Mongo.is_valid('507f1f77bcf86cD799439011')  # False (we arbitrarily only allow lowercase letters)
# The timestamp method will return a date/time object from the timestamp of the Mongo string and false otherwise:

# # Mongo.get_timestamp should return a datetime object

# Mongo.get_timestamp('507f1f77bcf86cd799439011')  # Wed Oct 17 2012 21:13:27 GMT-0700 (Pacific Daylight Time)
# Mongo.get_timestamp('507f1f77bcf86cz799439011')  # False
# Mongo.get_timestamp('507f1f77bcf86cd79943901')   # False
# Mongo.get_timestamp('111111111111111111111111')  # Sun Jan 28 1979 00:25:53 GMT-0800 (Pacific Standard Time)
# Mongo.get_timestamp(111111111111111111111111)    # False
# When you will implement this correctly, you will not only get some points, but also would be able to check creation time of all the kata here :-)


from datetime import datetime

class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        if type(s) != str: #should be a string
            return False
        elif len(s) != 24: #should be 12 bytes
            return False
        elif any(True for c in s if c not in "1234567890abcdef"): #should be hexadecimal
            return False
        else: 
            return True
    
    @classmethod
    def get_timestamp(cls, s):
        if cls.is_valid(s):
            return datetime.fromtimestamp(int(s[:8],16))
        else:
            return False


# Alternative solution
# from datetime import datetime
# import re

# class Mongo(object):

#     @classmethod
#     def is_valid(cls, s):
#         return isinstance(s,str) and bool(re.match(r"[a-f0-9]{24}$",s))
    
#     @classmethod
#     def get_timestamp(cls, s):
#         return cls.is_valid(s) and datetime.fromtimestamp(int(s[:8],16))