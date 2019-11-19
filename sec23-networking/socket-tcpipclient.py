import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
s.connect(("localhost", 4000))

# Receive server msgs
msg = s.recv(1024)

# Looping as long as the message keeps coming
while msg:
    # Decode the message
    print("Received: ", msg.decode())
    msg = s.recv(1024)

s.close()