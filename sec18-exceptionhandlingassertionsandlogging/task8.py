class InvalidPasswordException(Exception):
    def __init__(self, msg):
        self.msg = msg

def validatePassword(password):
    if len(password) < 8:
        raise InvalidPasswordException("The entered password is not valid")
    print("Valid password")


password = input("Enter a password:")
try:
    validatePassword(password)
except InvalidPasswordException as obj:
    print(obj)

