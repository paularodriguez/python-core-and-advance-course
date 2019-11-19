import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
s.connect(("localhost", 6767))

filename = input("Enter a file name:")

# Send the name of the file encoded
s.send(filename.encode())

# Receive server msgs
content = s.recv(1024)

# Decode the received content
print(content.decode())

s.close()