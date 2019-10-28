# Decorator that doubles the number returned

def decor(fun):
    def inner():
        return fun() * 2
    return inner

# def num():
#     return 5
#
# resultfun = decor(num)
#
# print(resultfun())


# Apply @decor

@decor
def num():
    return 5

print(num())