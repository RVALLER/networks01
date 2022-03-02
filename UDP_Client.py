# This will be the UDP Client program for socket Programming
from socket import *

# Server name can be the hostname (cs.bridgew.edu) or IP address
# localhost or 127.0.0.1 refers to local computer
server_name = 'localhost'
server_port = 12000
# SET UP SOCKET, AF_INET for IPV4 address, SOCK_DGRAM for UDP protocol
client_socket = socket(AF_INET, SOCK_DGRAM)

# Read the Message from the User
message = input("Input lower-case sentence: ")
client_socket.sendto(message.encode(), (server_name, server_port))
modified_message, server_address = client_socket.recvfrom(2048)
print(modified_message.decode())
client_socket.close()