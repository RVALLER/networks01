# This will be the TCP Client program for socket Programming
from socket import *

# Server name can be the hostname (cs.bridgew.edu) or IP address
server_name = 'localhost'
# localhost or 127.0.0.1 refers to local computer
server_port = 14000

# SET UP SOCKET, AF_INET for IPV4 address, SOCK_DGRAM for TCP protocol
client_socket = socket(AF_INET, SOCK_STREAM)
# Initiate TCP connection with handshake
client_socket.connect((server_name, server_port))

# Read Message
message = input("Input a sentence: ")
client_socket.send(message.encode())
modified_message = client_socket.recv(2048)
print('From Server: ', modified_message.decode())
client_socket.close()
