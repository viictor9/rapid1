# import socket



# host = 'local host'
# port = 443


# s = socket.socket(socket.AF_INET,
# 				socket.SOCK_STREAM)


# s.connect(('127.0.0.1', port))


# msg = s.recv(1024)


# while msg:
# 	print('Received:' + msg.decode())
# 	msg = s.recv(1024)


# s.close()


import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server's IP address and port
server_address = ('localhost', 8080)  # Make sure this matches the server's address and port
client_socket.connect(server_address)

# Receive data from the server
server_data = client_socket.recv(1024).decode()
print(f"Received from server: {server_data}")

# Send a message to the server
message = "Hello, server! This is the client."
client_socket.send(message.encode())

# Close the client socket
client_socket.close()
