# + -> One or more repetitions
# \d+ -> One or more digits

# * -> Zero or more repetitions

# ? -> Zero or one repetition

# {m} -> M repetitions

# {m,n} -> Indicated maximum and minimum repetitions

import re

str = "Take up one idea. One idea at a time only"

# Find 'o' followed by one or more alphanumeric characters
result = re.findall(r'o\w+', str)
print(result)

# Find 'o' followed by zero or more alphanumeric characters
result = re.findall(r'o\w*', str)
print(result)

# Find 'o' followed by zero or one alphanumeric characters
result = re.findall(r'o\w?', str)
print(result)

# Find 'o' followed by {2} alphanumeric characters
result = re.findall(r'o\w{3}', str)
print(result)

# Find 'o' followed by {2} alphanumeric characters
result = re.findall(r'o\w{2,3}', str)
print(result)



