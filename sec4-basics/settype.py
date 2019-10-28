# It doesn't allow duplicates
s = {10, 20, 30, "XYZ", 10, 20, 30}
print(s)
print(type(s))

s.update([88, 99])
print(s)

s.remove(30)
print(s)

f = frozenset(s)
# Not allowed
#f.update([10])
print(f)