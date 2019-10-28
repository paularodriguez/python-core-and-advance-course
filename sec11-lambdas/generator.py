def customgen(x,y):
    while x<y:
        yield x
        x+=1

result = customgen(1,10)

for i in result: print(i)