import socket
import threading

# Define the host and port to listen on
host = '127.0.0.1' #localhost
port = 55555

# Create a socket object, with the IP address family (AF_INET) and socket type (SOCK_STREAM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server.bind((host, port))

# Start listening for incoming connections
server.listen()

# Keep track of connected clients
clients = []
nicknames = []

# Function to broadcast a message to all clients
def broadcast(message):
    for client in clients:
        client.send(message)
    
# Function to handle a connected client
def handle(client):
    while True:
        try:
            # Receive a message from the client
            message = client.recv(1024)
            
            # Print the message to the console
            print(f"{nicknames[clients.index(client)]} says {message}")
            
            # Broadcast the message to all clients
            broadcast(message)
        except:
            # In case of an error, remove the client from the clients list
            index = clients.index(client)
            clients.remove(client)
            client.close()
            
            # Remove the nickname of the client as well
            nickname = nicknames[index]
            nicknames.remove(nickname)
            
            # Broadcast a message to the chat to inform that the client has left
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            break

# Function to receive incoming connections
def receive():
    while True:
        # Accept incoming connections
        client, address = server.accept()
        print(f"connected with {str(address)}")

        # Send a message to the client to request a nickname
        client.send('Messi'.encode('utf-8'))
        nickname = client.recv(1024)
        
        # Add the nickname to the list of nicknames
        nicknames.append(nickname)
        
        # Add the client to the list of clients
        clients.append(client)

        print(f'username of the client is {nickname}!')
        
        # Broadcast a message to the chat to inform that the client has joined
        broadcast(f'{nickname} joined the chat'.encode('utf-8'))
        
        # Send a message to the client to confirm the connection
        client.send('connected to the server!'.encode('utf-8'))

        # Start a new thread to handle the client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Inform the console that the server is listening for connections
print("Server is listening")

# Start the receive function to accept incoming connections
receive()
