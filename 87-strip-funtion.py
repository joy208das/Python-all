""".strip() Method Tutorial
The .strip() method in Python is used to remove
leading and trailing whitespace (spaces, tabs, newlines) from a string. 
It can also be used to remove specific characters
from both ends of a string if provided."""


s = "   Hello, World!   "
result = s.strip()
print(result)  # Output: "Hello, World!"

'''Removing Specific Characters'''
s = "xxHello, World!xx"
result = s.strip('x')
print(result)  # Output: "Hello, World!"

