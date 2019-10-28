s="    You are awesome   "
print(s)

s1="""You are 
the creator 
of your destiny
"""
print(s1)

print(s[0])

#Slicing
print(s[0:3])
print(s[3:])
print(s[:3])
print(s[-3:-1])

#Slicing steps
print(s[0:10:2])
print(s[15::-1])

#Strip spaces
print(s.strip())
print(s.lstrip())
print(s.rstrip())

#Find
print(s.find("You", 1))
print(s.count("a"))
print(s.replace("You", "We"))
print(s.upper())
print(s.lower())
print(s.title())

#Exercise
a=10
b=20.54
c=True
d="I am the best"

print(a)
print(b)
print(c)
print(d)