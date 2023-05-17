import unittest, socket, datetime
from unittest.mock import patch
import Server
import Client

@patch("socket.socket")

def test_file_contents(self, mock_socket):

    sock_server = mock_socket.return_value
    sock_client = mock_socket.return_value

    Server.server()
    Client.client()

    mock_socket.assert_called_with(socket.AF_INET, socket.SOCK_STREAM)
    sock_server.bind.assert_called_with(("localhost", 16021))

    sock_server.listen.assert_called_with(1)
    sock_client.connect.assert_called_with(("localhost", 16021))

    sock_client.recv.assert_called_with(1)
    mock_socket.assert_called_with(socket.AF_INET, socket.SOCK_STREAM)
    
    dateReceive = datetime.datetime.now().date()
    message = "Sending to server data"
    print(dateReceive)
    sock_client.send.assert_called_with(message.encode())

    self.assertEqual(sock_client.recv.assert_called_with(1024), b"2023-05-17")   
    #self.assertEqual(Client, )

if __name__ == "main":
    unittest.main()

# client
import socket, datetime, Server
# asks server address

port = 16021
data_payload = 1024
host = 'localhost'
# Create a UDP socket 
sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def client(port): 
 
    server_address = (host, port) 
    print ("Connecting to %s port %s" % server_address) 

    try: 
            # client sends current
            message = "Sending to server data"

            #current_hour = now.strftime("%H:%M:%S") 
            print ("Sending %s" % message) 
            # send 3 messages to server
            sent = sock_client.sendto(message.encode('utf-8'), server_address) 
    
            # Receive response 
            data, server = sock_client.recvfrom(data_payload) 
            # returns received messages from server
            print ("received %s" % data) 

    # close client 
    finally: 
        print ("Closing connection to server") 
        sock_client.close() 


if __name__ == '__main__': 
     client(port)
# server
import socket, datetime
# atender de forma continua sin close()
# accept conexions of every client

host = 'localhost'
data_payload = 1024
port = 16021
  # Create a socket UDP
sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

def  server(port):  
 
    # Bind socket to port 
    server_address = (host, port) 
    print ("Launch server on %s port %s" % server_address) 
 
    sock_server.bind(server_address) 

    while True: 
        print ("Waiting to receive petition from client") 
        data, address = sock_server.recvfrom(data_payload) 
        print ("Data: %s" %data) 
     
        if data: 
            nowDate = datetime.datetime.now().date()
            nowDate = "%s"%(nowDate)
            sent = sock_server.sendto(nowDate.encode('utf-8'), address)
            #  data, server = sock.recvfrom(data_payload) 
            print ("sent %s bytes back to %s" % (sent, address)) 

if __name__ == '__main__': 
     server(port)
