import socket

sock = socket.socket()
print("Socket created")

port = 1989

sock.bind(('', port))
print("Socket bound to %s" %(port))

sock.listen(5)
print("Socket listening")

while True:
    c, addr = sock.accept()
    print("Conntected to", addr)
    



