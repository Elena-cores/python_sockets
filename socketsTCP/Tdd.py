#server sends time
import socket
import time

def send_current_time(client_socket):
    current_time = time.ctime().encode()
    client_socket.send(current_time)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(1)
    print("Server is listening on localhost:12345")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client: {client_address}")

        send_current_time(client_socket)

        client_socket.close()

if __name__ == "__main__":
    start_server()

#client

import socket

def receive_current_time(server_socket):
    current_time = server_socket.recv(1024).decode()
    return current_time

def start_client():
    server_address = ("localhost", 12345)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    current_time = receive_current_time(client_socket)
    print(f"Current time received: {current_time}")

    client_socket.close()

if __name__ == "__main__":
    start_client()

 #prueba

import unittest
from unittest.mock import patch
import server
import client

class TestSocketCommunication(unittest.TestCase):
    @patch("socket.socket")
    def test_send_receive_current_time(self, mock_socket):
        server_socket = mock_socket.return_value
        client_socket = mock_socket.return_value

        server.start_server()
        client.start_client()

        mock_socket.assert_called_with(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind.assert_called_with(("localhost", 12345))
        server_socket.listen.assert_called_with(1)
        client_socket.connect.assert_called_with(("localhost", 12345))

        server_socket.send.assert_called_with(server.time.ctime().encode())
        client_socket.recv.assert_called_with(1024)

        # Realiza las comprobaciones específicas que deseas sobre la hora actual recibida

if __name__ == "__main__":
    unittest.main()

