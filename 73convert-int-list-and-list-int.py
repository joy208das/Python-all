'''convert int to list'''
n = 121

# Convert the integer to a string, then map each character back to an integer
digits = list(map(int, str(n)))

print(digits)  # Output: [1, 2, 1]

"""convert list to integer"""
a = [1, 2, 3]
b = int("".join(map(str, a)))  # Convert each element to a string, join them, and then convert to an integer
print(b)  # Output: 123