# server.py
import socket

IP_ADDR = '127.0.0.1'
UDP_PORT = 9090
BUFFER_SIZE = 1024

clients = {}


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((IP_ADDR, UDP_PORT))

print("server is running")

while True:
    data, addr = server_socket.recvfrom(BUFFER_SIZE)

    if data.startswith(b'GREETING'):
        # Register client
        clients[addr] = True
        print(f"Client {addr} has greeted.")

    elif data.startswith(b'MESSAGE'):
        
        message = data[8:].decode()  
        print(f"<From {addr[0]}:{addr[1]}>: {message}")

        for client_addr in clients.keys():
            server_socket.sendto(f'INCOMING<{addr[0]}:{addr[1]}>: {message}'.encode(), client_addr)
