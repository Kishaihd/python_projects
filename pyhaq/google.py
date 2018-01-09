import socket
import sys

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
except socket.error as err:
    print("Socket creation failed with error %s" %(err))


# Default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print("Error resolving host")
    sys.exit()

# Connecting to the server
sock.connect((host_ip, port))

print("Socket successfully connected to google on port %s" %(host_ip))






