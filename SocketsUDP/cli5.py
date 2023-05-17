import socket, argparse 
 
host = 'localhost' 
data_payload = 10000
 
def  client(port): 
    # Create a UDP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
 
    server_address = (host, port) 
    print ("Connecting to %s port %s" % server_address) 
 
    try: 
 
        # Send data 
        message = "Get date-time" 
        print ("Sending %s" % message) 
        sent = sock.sendto(message.encode
               ('utf-8'), server_address) 
 
        # Receive response 
        data, server = sock.recvfrom(data_payload) 
        print ("received %s" % data) 
 
    finally: 
        print ("Closing connection to server") 
        sock.close() 
 
 # launch as a script. Specify port you want to use 
if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='Socket Server UDP Example') 
    parser.add_argument('-port', action="store", dest="port", type=int, required=False) 
    given_args = parser.parse_args()  
    port = given_args.port 
    client(port) 