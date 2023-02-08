import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

# IP address and port number to connect to 
HOST = '127.0.0.1'
PORT = 55555

# Client class to handle GUI and communication with the server
class Client:
    def __init__(self, host, port):
        # Create a TCP socket and connect to the specified host and port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        # Popup dialog to get the user's nickname
        msg = tkinter.Tk()
        msg.withdraw()
        self.nickname = simpledialog.askstring("Nickname", "Please choose a Username", parent=msg)

        # Flags to keep track of the GUI and receive loop
        self.gui_done = False
        self.running = True

        # Start the GUI and receive loop in separate threads
        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)
        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        # Create the GUI window
        self.win = tkinter.Tk()
        self.win.configure(bg="lightgreen")

        # Chat label
        self.chat_label = tkinter.Label(self.win, text="chat:", bg="lightgrey")
        self.chat_label.config(font=("Ariel",12))
        self.chat_label.pack(padx=25, pady=5)

        # Text area to display chat messages
        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state='disabled')

        # Message label
        self.msg_label = tkinter.Label(self.win, text="Message:", bg="lightgrey")
        self.msg_label.config(font=("Ariel", 12))                          
        self.msg_label.pack(padx=20, pady=5)
        
        # Input area for the user to type their messages
        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)
        
        # Send button to send the message
        self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
        self.send_button.config(font=("Ariel", 12))
        self.send_button.pack(padx=20, pady=5)
        
        # Update the flag to indicate that the GUI is done initializing
        self.gui_done = True
        
        # Handle window close event
        self.win.protocol("WM_DELETE_WINDOW", self.stop)
        
        # Start the GUI loop
        self.win.mainloop()
        
   
# This script defines methods for a Client class in a chat application

def write(self):
    # This method sends a message to the server by encoding it in utf-8
    message = f'{self.nickname}: {self.input_area.get("1.0", "end")}'
    self.sock.send(message.encode('utf-8'))
    # Clearing the input area after the message has been sent
    self.input_area.delete('1.0', 'end')

def stop(self):
    # This method stops the chat application by setting running to False, 
    # destroying the window and closing the socket
    self.running = False
    self.win.destroy()
    self.sock.close()
    # Exiting the program
    exit(0)

def receive(self):
    # This method receives messages from the server and updates the chat window
    while self.running:
        try:
            message = self.sock.recv(1024)
            if message == 'Messi':
                # If the message is NICK, the client sends its nickname to the server
                self.sock.send(self.nickname.encode('utf-8'))
            else:
                # If the message is not NICK, it is displayed in the chat window
                if self.gui_done:
                    self.text_area.config(state='normal')
                    self.text_area.insert('end', message)
                    # Scrolling to the end of the chat window
                    self.text_area.yview('end')
                    self.text_area.config(state='disabled')
        except ConnectionAbortedError:
            break
        except: 
            # Printing an error message if an exception is encountered
            print("Error")
            self.sock.close()
            break

# Creating a Client object with the specified host and port
client = Client(HOST, PORT)
