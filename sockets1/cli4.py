# Echo client program
import socket, sys

socketPath = '/tmp/uds_socket'

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

print(sys.stderr, 'connecting to %s' % socketPath)
try:
    sock.connect(socketPath)
except socket.error as msg:
    print(sys.stderr, msg)
    sys.exit(1)

try:
    
    # Send data
    message = sys.argv[1]   # second argument
    print(sys.stderr, 'sending "%s"' % message)
    sock.send(message.encode('utf-8'))
    
    while True:
        data = sock.recv(1024)
        if data:
            print(data)
        else:
            print(data)
            break
    print('no receiving data from server anymore')

finally:
    print(sys.stderr, 'closing socket')
    sock.close()
