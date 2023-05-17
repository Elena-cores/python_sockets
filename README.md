# python_sockets


server

import socket

def get_file_path(client_socket):

    file_path = "path/to/your/file.txt"

    client_socket.send(file_path.encode())

def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(("localhost", 12345))

    server_socket.listen(1)

    print("Server is listening on localhost:12345")

    while True:

        client_socket, client_address = server_socket.accept()

        print(f"Connected to client: {client_address}")

        get_file_path(client_socket)

        client_socket.close()

if __name__ == "__main__":

    start_server()


client
import socket

def receive_file_path(server_socket):

    file_path = server_socket.recv(1024).decode()

    return file_path

def check_file_contents(file_path):

    with open(file_path, "r") as file:

        file_contents = file.read()

        return file_contents

def start_client():

    server_address = ("localhost", 12345)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(server_address)

    file_path = receive_file_path(client_socket)

    file_contents = check_file_contents(file_path)

    print(f"File contents: {file_contents}")

    client_socket.close()

if __name__ == "__main__":

    start_client()




test

import unittest

from unittest.mock import patch

import server

import client

class TestFileContents(unittest.TestCase):

    @patch("socket.socket")

    def test_file_contents(self, mock_socket):

        server_socket = mock_socket.return_value

        client_socket = mock_socket.return_value

        server.start_server()

        client.start_client()

        mock_socket.assert_called_with(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.bind.assert_called_with(("localhost", 12345))

        server_socket.listen.assert_called_with(1)

        client_socket.connect.assert_called_with(("localhost", 12345))

        mock_socket.assert_called_with(socket.AF_INET, socket.SOCK_STREAM)

        client_socket.send.assert_called_with("path/to/your/file.txt".encode())

        client_socket.recv.assert_called_with(1024)

        self.assertEqual(client.check_file_contents.call_args[0][0], "path/to/your/file.txt")

if __name__ == "__main__":

    unittest.main()


