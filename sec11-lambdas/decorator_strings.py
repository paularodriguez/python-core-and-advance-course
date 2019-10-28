# The hello function takes a name and it will return Hello under that name and then even create a decorator
# function called howareyou that will take the result of the hello function and it will append a string
# called "How are you" at the end

# Hello (name)
# howareyou()

def howareyou(fun):
    def inner(n):
        return fun(n) + " How are you?"
    return inner

@howareyou
def hello(name):
    return "Hello " + name

print(hello("Paula"))
