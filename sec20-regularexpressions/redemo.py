import re

str = "Take up one idea.One idea at a time"

# Find 'o' followed by any two characters
result = re.search(r'o\w\w', str)

# Returns 'one', the first substring that matches
print(result.group())

# Find 'o' followed by any one character
result = re.search(r'o\w', str)
print(result.group())
