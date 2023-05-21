# client.py

import socket

def request_time(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.send('ACK'.encode())

    response = client_socket.recv(1024).decode()
    print("Current time:", response)

    client_socket.close()

if __name__ == '__main__':
    request_time('localhost', 8001)