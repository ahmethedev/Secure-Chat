# client.py
import socket

IP_ADDR = '127.0.0.1'
UDP_PORT = 9090
BUFFER_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


client_socket.sendto(b'GREETING', (IP_ADDR, UDP_PORT))
print("Greeted the server.")

while True:
    message = input("] Prompt message from user\n")
    client_socket.sendto(b'MESSAGE' + message.encode(), (IP_ADDR, UDP_PORT))

    data, addr = client_socket.recvfrom(BUFFER_SIZE)
    print(data.decode())
