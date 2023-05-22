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
    
    
 
from builtins import list

def read_request(request):
    request_message = request.split(" ")
    letters = list(request)
    if (request_message[0] == "Phrase"):
        message = request_message[1]
        inverseWord = message[::-1] 
        if inverseWord == message:
            return "SI"
        elif (len(letters) != len(set(letters))) or len(letters) <= 10:     # if theres duplicates in word-> parcial or word is 3 letters
             return "PARCIAL"
        else: 
            return str(len(letters))
        #message = "ana"
    elif (request_message[0] == "Number"):
        message = request_message[1]
        inverseWord = message[::-1]
        if inverseWord == message:
            return "SI"
        elif type(inverseWord) != int:
            return "NONATURAL"
        else: 
            return "NO"


 
import unittest, socket
from Manager import *

class Test(unittest.TestCase):
    def test_setUp(self):
        self.host = 'localhost'
        self.port = 16020
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))
        
    # Possible solutions -> SI = palíndromo puro, NO = Palíndromo no puro, Parcial
    def test_palindromo1(self):
        palindromo = "Phrase ana"
        respuesta = read_request(palindromo)
        self.assertEqual("SI", respuesta)
    
    def test_not_palindromo1(self):
        palindromo = "Phrase hola"
        respuesta = read_request(palindromo)
        self.assertEqual("NO", respuesta)
    
    def test_numeroCapicua(self):
        capicua = "Number 13431"
        respuesta = read_request(capicua)
        self.assertEqual("SI", respuesta)
    
    def test_not_numeroCapicua(self):
        capicua = "Number 13422"
        respuesta = read_request(capicua)
        self.assertEqual("NO", respuesta)
    
    def test_not_numeroNatural(self):
        capicua = "Number 1342a"
        respuesta = read_request(capicua)
        self.assertEqual("NONATURAL", respuesta)
    
    def test_palindromoParcial1(self):
        palindromo = "Phrase anas"
        respuesta = read_request(palindromo)
        self.assertEqual("PARCIAL", respuesta)
