### Type of Errors ###

# Syntax Error
# print "¡Hello World!" # Error

from math import pi
import math

print("¡Hello World!")

# Name Error
# print(number) # Error
language = "English"
print(language)

# Index Error
my_list = ["Antony", "Jordan", "Lima", 30]
print(my_list[0])
print(my_list[-1])
# print(my_list[5]) # Error

# Module not found error
# import match # Error

"""import math"""
"""import datetime"""

# Attribute error
# print(math.PI) # Error
print(math.pi)

# Key error
my_dict = {"Name": "Antony", "Value": 50, "Type": "Person"}
print(my_dict["Value"])
# print(my_dict[0]) # Error
# print(my_dict["Typ"]) # Error

# Type error
# print(my_list["Name"]) # Error
print(my_list[0])

# Import error
# from math import PI # Error
print(pi)

# Value error
# my_int = int("10 Age") # Error
my_int = int("10")
print(my_int)


# Zero Division Error
print(4 / 2)
# print(4 / 0) # Error
