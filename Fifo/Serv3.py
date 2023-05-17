import os, sys, time, datetime

pathFifoServerToClient = "/tmp/fifoServerToClient"
pathFifoClientToServer = "/tmp/fifoClientToServer"

os.mkfifo(pathFifoClientToServer)
os.mkfifo(pathFifoServerToClient)

with open(pathFifoClientToServer) as fo:
    buffer = fo.read()
    
if buffer == "date":
    actualDate = datetime.datetime.now()

    fd = os.open(pathFifoServerToClient, os.O_WRONLY)
    bDate = "%s"%(actualDate)

    os.write(fd, bDate.encode('utf8'))
    os.close(fd)

