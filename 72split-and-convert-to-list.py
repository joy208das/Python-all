num = input("enter :").split()
print(num)

a = list(num)
print(a)
nums = list(map(int, input("Enter the numbers in the array, separated by spaces: ").split()))


'''Method: .split()
Purpose: This string method splits the input string into a list of substrings based on a delimiter. By default, .split() uses any whitespace (spaces, tabs, newlines) as the delimiter.
Behavior: Converts the single string into a list where each element is a separate string representing a number.

Function: list()
Purpose: Converts the map object (which is an iterator) into a list.
Behavior: Materializes the entire iterator into a list containing the converted integer values.

'''