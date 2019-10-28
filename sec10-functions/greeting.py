def display(name):
    def message():
        return "Hello "

    return message() + name

print(display("Paula"))