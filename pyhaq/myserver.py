

import socket 

sock = socket.socket()
print("Socket created")

# Reserve a port number
port = 2345

# Bind to port.
sock.bind(('', port))
print("Socket bound to port %s" %(port) )

# Put socket into listening mode
sock.listen(5)
print("Socket listening")

# Create a loop to run until exit or error.
while True:
    # Establish connection with client
    c, addr = sock.accept()
    print("Connected to ", addr)


