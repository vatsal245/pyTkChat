import socket
import threading
import sys
import os
from tkinter import *

def recv_messages(c):
        while True:
            data = c.recv(1024).decode('utf-8')
            message_text.insert(INSERT, '\nCLIENT: {}'.format(data))

def send_msgs():
    c = conn
    data = inp.get()
    c.send(bytes(data, 'utf-8'))
    message_text.insert(INSERT, '\nYOU: {}'.format(data))

def quit_end():
    conn.close()
    sys.exit()

host= '127.0.0.1'
port = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen(2)
print('server started, waiting for client to connect...')
conn, addr = server.accept()

root = Tk()
root.title('TkChat.')
root.config(bg = '#000000')
message_text = Text(root, width = 50)
message_text.grid(row = 0, column = 0, padx = 10, pady = 10)
message_text.insert(INSERT,'Established connection successfully.\n')
message_text.insert(INSERT,'Client is at {}'.format(addr))
message_text.insert(INSERT, '\n------------------------------------------------')
inp = Entry(root, width = 50)
inp.grid(row = 1, column = 0, padx = 10, pady = 10)
btn = Button(text = 'Send!!', command = send_msgs)
btn.grid(row = 2, column = 0, padx = 10, pady = 10)
btn.config(bg = '#dd0000', fg = '#ffffff')
btn1 = Button(text = 'Quit!', command = quit_end)
btn1.config(bg = '#dd0000', fg = '#ffffff')
btn1.grid(row = 3, column = 0, padx = 10, pady = 10)
thread1 = threading.Thread(target = recv_messages, args = (conn, ))
thread1.start()
root.mainloop()


