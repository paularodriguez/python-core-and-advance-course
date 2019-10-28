#Ask user to enter a number
#Display all the numbers up to that number
#Skip the multiple of 10
#Stop if number is > 100

x = int (input("Enter one number"))

i = 0
while i < x:
    i+=1;
    if i > 100:
        break
    elif i%10 == 0:
        continue
    else:
        print(i)
