data = ['a', 'ab', 'a', 'ab', 'ab']

# Find the most common element
most_common_element = max(set(data), key=data.count)

print(most_common_element)  # Output: ab
