import re

str = "Take 1 up one 23 idea.one idea 45 at a time"

# FIND

# Find 'o' followed by any two characters
result = re.search(r'o\w\w', str)

# Returns 'one', the first substring that matches
print(result.group())

# Find 'o' followed by any one character
result = re.search(r'o\w', str)
print(result.group())

# No results -> None

# SEARCH

# Search 'o' followed by any two characters
# Returns one list with all found substrings
result = re.findall(r'o\w\w', str)

print(result)

# No results -> Empty list []

# MATCH
# Match method only searches at the beginning of the given string
result = re.match(r'o\w\w', str)
print(result)

result = re.match(r'T\w\w', str)
print(result.group())

# SPLIT
# Split the string when there are digits
result = re.split(r'\d+', str)
print(result)

# Substitute
# It works like a replaceAll
result = re.sub(r'one', 'two', str)
print(result)


