import unittest
import socket
from server import get_current_time, start_server

class ServerTestCase(unittest.TestCase):
    def setUp(self):
        self.host = 'localhost'
        self.port = 8000
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)

    def tearDown(self):
        self.server_socket.close()

    def test_get_current_time(self):
        current_time = get_current_time()
        self.assertIsNotNone(current_time)

    def test_server_response_with_valid_ack(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))
        client_socket.send('ACK'.encode())
        response = client_socket.recv(1024).decode()
        client_socket.close()
        self.assertIsNotNone(response)
        self.assertRegex(response, r'\d{2}:\d{2}:\d{2}')

    def test_server_response_with_invalid_ack(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))
        client_socket.send('ACK'.encode())
        response = client_socket.recv(1024).decode()
        client_socket.close()
        self.assertIsNotNone(response)
        self.assertTrue(response.startswith('Mon') or response.startswith('Tue') or response.startswith('Wed') or response.startswith('Thu') or response.startswith('Fri') or response.startswith('Sat') or response.startswith('Sun'))
        #pass

    def test_server_response_with_invalid_ack(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))
        client_socket.send('INVALID'.encode())
        response = client_socket.recv(1024).decode()
        client_socket.close()
        self.assertEqual(response, '')
        #pass

    def test_server_shutdown(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))
        client_socket.send('ACK'.encode())
        client_socket.recv(1024).decode()
        client_socket.close()
        self.assertRaises(KeyboardInterrupt, start_server, self.host, self.port)

if __name__ == '__main__':
    unittest.main()

#if __name__ == '__main__':
    # loader = unittest.TestLoader()
    # suite = unittest.TestSuite()
    # suite.addTests(loader.loadTestsFromTestCase(ServerTestCase))
    # runner = unittest.TextTestRunner(verbosity=2)
    # result = runner.run(suite)