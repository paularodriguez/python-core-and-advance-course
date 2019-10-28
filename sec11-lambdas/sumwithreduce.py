from functools import reduce

# Using the reduce function to find out the sum of all elements in a list

lst = [1,3,5]

result = reduce(lambda x,y:x+y, lst)

print(result)
