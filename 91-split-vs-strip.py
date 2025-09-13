""""1. split() vs strip()
split():
Purpose: Splits a string into a list of substrings 
based on a delimiter (default is whitespace).

Example:


s = "hello world"
result = s.split()  # Splits into ['hello', 'world']

Behavior:

If you use split() on a string like "tour", 
it will split the string into a list of words. 
Since there are no spaces in "tour", it will return ['tour'].

If you use split() on "hello world", it will return ['hello', 'world'].

strip():
Purpose: Removes leading and trailing whitespace (or specified characters) from a string.

Example:


s = "  hello world  "
result = s.strip()  # Removes leading/trailing spaces: "hello world"
Behavior:

If you use strip() on " tour ", it will return "tour" (removes spaces).

If you use strip() on "tour", it will return "tour" (no spaces to remove).

and if we run result[0] it will return 'h'

"""