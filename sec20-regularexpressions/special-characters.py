# Special characters

# \ -> to use \ itself or any other special character
# . -> Dot operator, matches any character except a new line
# ^ -> Match a regular expression at the beginning of a string
# $ -> Match a regular expression at the end of a string
# [...] -> To specify a range of values
# [^...] -> To exclude a range of values
# (...) -> Provide a regular expression
# (A | B) -> Pipe symbol to specify multiple regular expressions

import re

str = "Take up one 1-10-2019 idea. One idea at 12 a time 12-11-2019 only"

# Carrot symbol ^ -> Regex should match at the beginning of the string
result = re.search(r'^T\w*', str)
print(result.group())
# Take

result = re.search(r'^O\w*', str)
print(result)
# None

