# import socket


# host = ''
# port = 443


# s = socket.socket(socket.AF_INET,
# 				socket.SOCK_STREAM)


# s.bind(('', port))


# s.listen(1)


# c, addr = s.accept()


# print("CONNECTION FROM:", str(addr))


# c.send(b"HELLO, How are you ? \
# 	Welcome to Akash hacking World")

# msg = "Bye.............."
# c.send(msg.encode())

# c.close()


import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8080)  # You can choose a different port if needed
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening for incoming connections...")

# Wait for a connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Send a message to the client
message = input("Enter the message to send to the client: ")
client_socket.send(message.encode())

# Receive data from the client
data = client_socket.recv(1024).decode()
print(f"Received from client: {data}")

# Close the client socket
client_socket.close()

# Close the server socket
server_socket.close()
