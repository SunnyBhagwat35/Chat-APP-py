import socket

HEADER = 64#tells us the length of the  msg 
PORT = 5050
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
DISCONNECT_MSG = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length =  str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length ))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

while 1:
    send(input())
