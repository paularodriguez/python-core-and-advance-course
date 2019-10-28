# print from 1 to 20 skip multiples of 3

#For loop
for i in range(1,21):
    if(i%3 == 0):
        continue
    print(i)

#While loop
x = 0
while x <= 20:
    x+=1
    if x%3 == 0:
        continue
    print(x)

