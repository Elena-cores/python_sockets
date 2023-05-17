import socket, argparse
from datetime import datetime

 
host = 'localhost' 
data_payload = 2048 
 
def  server(port):  
    # Create a socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
 
    # Bind socket to port 
    server_address = (host, port) 
    print ("Launch server on %s port %s" % server_address) 
 
    sock.bind(server_address) 
 
    while True: 
        print ("Waiting to receive petition from client") 
        data, address = sock.recvfrom(data_payload) 
        print ("Data: %s" %data) 
     
        if data: 
            sent = sock.sendto(str(datetime.now()).encode('utf-8'), address)
            print ("sent %s bytes back to %s" % (sent, address)) 
 
 
if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='Socket Server UDP Example') 
    parser.add_argument('-port', action="store", dest="port", type=int, required=False) 
    given_args = parser.parse_args()  
    port = given_args.port 
    server(port) 