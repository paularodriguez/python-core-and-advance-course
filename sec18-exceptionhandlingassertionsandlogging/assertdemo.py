try:
    num = int(input("Enter an even number: "))
    assert num%2 == 0, "You have entered an odd number"
except AssertionError as ob:
    print(obj)

print("After the exception")