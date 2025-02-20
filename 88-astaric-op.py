# Without *
a = [1, 2, 3]
b = [4, 5]
result = [a, b]
print(result)  # Output: [[1, 2, 3], [4, 5]]

# With *
result = [*a, *b]
print(result)  # Output: [1, 2, 3, 4, 5]