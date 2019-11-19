import socket

host = 'localhost'
port = 6767

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

print("Server listening on port: ", port)

s.listen(1)

c, addr = s.accept()

# Get the name of the file from the client
fileName = c.recv(1024)

# Open the file and read it as binary
try:
    f = open(fileName, 'rb')
    content = f.read()
    c.send(content)
    f.close()
except FileNotFoundError:
    c.send(b"File does not exist")

c.close()