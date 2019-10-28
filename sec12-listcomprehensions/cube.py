# Cube of integers from 1 to 10


# Without list comprehension

lst = []

for x in range(1,11):
    lst.append(x**3)

print(lst)

# Using list comprehension

lst = []
lst = [x**3 for x in range(1,11)]

print(lst)