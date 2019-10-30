class OverTheLimitException(Exception):
    def __init__(self, msg):
        self.msg = msg

def checkNumber(number):
    if number > 100:
        raise OverTheLimitException("Given number is over the limit")

checkNumber(200)
