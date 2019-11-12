import re

str = "Take up one 1-10-2019 idea. One idea at 12 a time 12-11-2019 only"

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str)

print(result)