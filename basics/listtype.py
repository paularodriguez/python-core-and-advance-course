lst=[10,20,"Paula",-10, 30.5]
print(lst)

#Basic fn
print(lst[3])
print(lst[3:5])
print(lst*4)
print(len(lst))

#Add and remove elements
lst.append(40)
print(lst)

lst.remove("Paula")
del(lst[1])
print(lst)

#More useful methods
#lst.clear()
print(lst)
print(max(lst))
print(min(lst))

lst.insert(3,99)
print(lst)

lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)