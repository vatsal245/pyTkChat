import socket
import sys
import os
import threading
from tkinter import *

def receive_msg():
    while True:
        data = client.recv(1024)
        message_text.insert(INSERT, '\nCLIENT: {}'.format(data.decode('utf-8')))

def send_msgs():
    data = inp.get()
    client.send(bytes(data, 'utf-8'))
    message_text.insert(INSERT, '\nYOU: {}'.format(data))
def quit_end():
    client.close()
    sys.exit()
    
host= '127.0.0.1'
port = 12345
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

thread = threading.Thread(target = receive_msg)
thread.start()
    
root = Tk()
root.title('TkChat.')
root.config(bg = "#000000")
message_text = Text(root, width = 50)
message_text.grid(row = 0, column = 0, padx = 10, pady = 10)
message_text.insert(INSERT,'Established connection successfully.\n')
message_text.insert(INSERT,'Connected to the server room.')
message_text.insert(INSERT, '\n------------------------------------------------')
inp = Entry(root, width = 50)
inp.grid(row = 1, column = 0, padx = 10, pady = 10)
btn = Button(text = 'Send!!', command = send_msgs)
btn.grid(row = 2, column = 0, pady = 10)
btn.config(bg = "#dd0000", fg = "#ffffff")
btn1 = Button(text = 'Quit!', command = quit_end)
btn1.grid(row = 3, column = 0, padx = 20, pady = 10)
btn1.config(bg = "#dd0000", fg = "#ffffff")
root.mainloop()
