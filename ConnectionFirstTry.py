''' This python program is my first try at establishing a connection
 between this program running on a server and an android app'''

# Importing all required libraries
import socket

# Creating a socker object.
s1 = socket.socket()

# binding the socket to a port in this computer.
s1.bind((socket.gethostname(), 1234))

