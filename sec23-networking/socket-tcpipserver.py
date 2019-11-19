import socket

host = 'localhost'
port = 4000

# Create socket

# socket.AF_INET -> Specify Internet Protocol v4 addresses
# socket.SOCK_STREAM -> Specify TCP IP communication
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the created socket to one host and port
s.bind((host, port))

print("Server listening on port: ", port)

# Start listening -> The parameter is the number of connections the server is going to accept
s.listen(1)

# Accept the client connection, returns the connection and the address from which the request came from
c, addr = s.accept()

print("Connection from: ", str(addr))

# 'b' is added to convert the content to binary
c.send(b"Hello, how are you")
# Other way of binary conversion
c.send("bye".encode())

c.close()