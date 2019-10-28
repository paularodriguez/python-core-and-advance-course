dict = {1: "Paula", 2: "Mery"}

print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())

for i in dict.keys():
    print(i, dict[i])

del(dict[1])
print(dict)