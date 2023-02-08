# PracticePyWSocket

## Chat Server

**###How*** it's related to cybersecurity ? actually it's not at all it's just practice in write code that i commit myself to do in order not to forget and rust my skills

This script creates a simple chat server using Python's socket module. The server listens on a specified IP address and port and allows multiple clients to connect and communicate with each other. The script also keeps track of connected clients and their nicknames.

### **Requirements**
```
Python 3.x
socket module
threading module
```
### **Usage**

**1)** Clone or download the repository.

**2)** Open a terminal window and navigate to the folder where the script is located.

**3)** Run the script using the following command:

```
python Serverside.py
```
**4)** Open another terminal window and run the client-side script to connect to the chat server.

**5)** Repeat step 4 for additional clients.

### **Script Explanation**

The script starts by importing the necessary modules: *socket* and *threading*.

Next, it sets the host IP address and port number to listen on. The host IP address is set to *127.0.0.1* (localhost) and the port number is set to  *55555* .

A socket object is then created using the socket module, with the IP address family *(AF_INET)* set to *socket.AF_INET* and the socket type *(SOCK_STREAM)* set to *socket.SOCK_STREAM*. The socket is then bound to the specified host and port using the *bind* method. The listen method is called to start listening for incoming connections.

Two lists are created to keep track of connected clients: clients and nicknames.

The broadcast function takes a message as an argument and sends the message to all connected clients.

The handle function takes a client argument and starts an infinite loop to receive messages from the client. The messages are printed to the console and broadcasted to all clients. If an error occurs while receiving a message, the client is removed from the clients list, the corresponding nickname is removed from the nicknames list, and a message is broadcasted to inform that the client has left the chat.

The receive function starts an infinite loop to accept incoming connections. When a connection is accepted, the client is requested to provide a nickname. The nickname is added to the nicknames list, the client is added to the clients list, and a message is broadcasted to inform that the client has joined the chat. A new thread is then started to handle the connected client using the handle function.

Finally, the script informs the console that the server is listening for connections and starts the receive function.

Client-side Script

To use the chat server, a client-side script is required to connect to the server and communicate with other clients. A simple client-side script can be created using the socket module in Python. The script connects to the server using the same IP address and port number specified in the chat server script. The script then sends and receives messages from the server to communicate with other clients in the chat.
