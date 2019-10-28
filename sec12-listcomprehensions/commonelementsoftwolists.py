# Common elements of two lists

a = [1,2,4,5,6,7,8,9,10]
b = [2,4,6,8,10]

# Traditional way
result = []

for i in a:
    if i in b:
        result.append(i)

print(result)

# List comprehensions way

result = [i for i in a if i in b]
print(result)