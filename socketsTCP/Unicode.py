#server 

import socket

def receive_file(client_socket):
    file_data = client_socket.recv(1024).decode()
    return file_data

def send_file_content(client_socket, file_content):
    client_socket.send(file_content.encode())

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(1)
    print("Server is listening on localhost:12345")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client: {client_address}")

        file_content = receive_file(client_socket)
        unicode_content = file_content.encode("utf-8").decode("unicode_escape")
        send_file_content(client_socket, unicode_content)

        client_socket.close()

if __name__ == "__main__":
    start_server()
    
    
#client
import socket

def send_file(client_socket, file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
        client_socket.send(file_content.encode())

def receive_file_content(client_socket):
    file_content = client_socket.recv(1024).decode()
    return file_content

def start_client(file_path):
    server_address = ("localhost", 12345)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    send_file(client_socket, file_path)
    file_content = receive_file_content(client_socket)
    print(f"File content received: {file_content}")

    client_socket.close()

if __name__ == "__main__":
    file_path = "path/to/your/file.txt"  # Specify the path to your file here
    start_client(file_path)
