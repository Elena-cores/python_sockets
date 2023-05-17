# Echo server program
import socket, os, sys


socketPath = '/tmp/uds_socket'

# Make sure the socket does not already exist
try:
    os.unlink(socketPath)
except OSError:
    if os.path.exists(socketPath):
        raise

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Bind the socket to the port
print(sys.stderr, 'starting up on %s' % socketPath)
sock.bind(socketPath)

# Listen for incoming connections
sock.listen()

while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print(sys.stderr, 'connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print(sys.stderr, 'received "%s"' % data)
            if data:
                with open(data, 'r') as file:
                    print(sys.stderr, 'sending data back to the client')
                    for line in file.readlines():
                        connection.sendall(line.encode('utf-8'))    # mientras tengas sigue enviando datos
                #connection.send(b'exit')
            else:
                print(sys.stderr, 'no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()