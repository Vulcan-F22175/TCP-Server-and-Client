import socket

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()

port= 444

clientsocket.connect(('', port)) #Enter Your IP Address in the quotation marks before debugging.

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))