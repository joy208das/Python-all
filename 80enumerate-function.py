fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(f"Index: {i}, Fruit: {fruit}")
    
"""example:leetcode-problem-23"""    
    
    
'''What does enumerate() do?
fruits = ["apple", "banana", "cherry"]: This is just a list of fruit names.

enumerate(fruits): This converts the list into an iterable
of index-value pairs. Each item in fruits is paired with its index.

For example:

The first item "apple" is paired with the index 0, so it becomes (0, "apple").
The second item "banana" is paired with the index 1, so it becomes (1, "banana").
And so on.
for i, fruit in enumerate(fruits)::

i: This variable holds the index from enumerate().
In this case, i will be 0 for the first iteration, 1 for the second, etc.
fruit: This variable holds the corresponding value (the actual fruit name).
For the first iteration, fruit is "apple", then "banana", and so on.
Inside the loop:

During each iteration, the print() function outputs both the index and the fruit name.'''