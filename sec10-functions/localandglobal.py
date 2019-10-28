# Global variable
x=123

def display():
    x = 678
    print(x)
    # Get global variable value when there are another local variable with the same name
    print(globals()['x'])

print(x)
display()

# Assign function to a variable

z = display
z()
z()
z()
z()