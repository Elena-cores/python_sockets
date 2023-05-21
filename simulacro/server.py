import socket
import time

def get_current_time():
    return time.ctime()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server started on {}:{}".format(host, port))

    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection established with", client_address)

        data = client_socket.recv(1024).decode()
        if data == 'ACK':
            response = get_current_time()
            client_socket.sendall(response.encode())
            
        client_socket.close()

if __name__ == '__main__':
    start_server('localhost', 8001)