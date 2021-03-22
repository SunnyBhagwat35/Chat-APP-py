import socket
import threading


HEADER = 64#tells us the length of the  msg 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            
            print(f"[{addr}] {msg}")
            conn.send("message received".encode(FORMAT))
    conn.close() 

def start():
    server.listen()
    print(f"[LISTENING] Server is litening on {SERVER}")
    while 1:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        #Subtracting start() thrad
        #means subtraccting own from it
        print(f"[ACTIVE CONNECTION] {threading.activeCount() - 1}")
        
        
print("Starting server")
start()
