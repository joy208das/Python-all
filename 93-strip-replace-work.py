""""Print a single number — the number of distinct letters in Anton's set.

Examples
InputCopy
{a, b, c}
OutputCopy
3
InputCopy
{b, a, b, a}
OutputCopy
2
InputCopy
{}
OutputCopy
0"""

s = input().strip('{}').replace(', ', '')
unique = set(s)
print(len(unique))



