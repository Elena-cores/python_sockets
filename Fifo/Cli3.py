import os, sys, time

pathFifoServerToClient = "/tmp/fifoServerToClient"
pathFifoClientToServer = "/tmp/fifoClientToServer"

fd = os.open(pathFifoClientToServer, os.O_WRONLY)
os.write(fd, b"date")
os.close(fd)

with open(pathFifoServerToClient) as fo:
    buffer = fo.read()
    print(buffer)
    