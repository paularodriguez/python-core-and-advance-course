# Retrieve only even numbers from a given list

lst = [1,2,3,4,5,6,7]

result = list(filter(lambda x: x%2 == 0, lst))

print(result)

for i in result:
    print(i)
