''''
List vs Dictionary
List:
Purpose: An ordered collection of items. 
Items are accessed by their index.

Example:

python
Copy
vowels = ['a', 'e', 'i', 'o', 'u']  # List of vowels
print(vowels[0])  # Output: 'a'
Behavior:

Lists are great for storing ordered data.

Checking if an item exists in a list 
(e.g., if char in vowels) is slower for large lists because it requires a linear search.

Dictionary:
Purpose: A collection of key-value pairs.
Keys are unique, and values are accessed by their keys.

Example:

python
Copy
vowels = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}  # Dictionary of vowels
print('a' in vowels)  # Output: True
Behavior:

Dictionaries are great for fast lookups. 
Checking if a key exists in a dictionary (e.g., if char in vowels) is very fast, even for large dictionaries.


'''