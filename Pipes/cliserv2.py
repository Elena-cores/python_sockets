import os, sys, time

rClientToServer, wClientToServer = os.pipe()
rServerToClient, wServerToClient = os.pipe()
frClientToServer, fwClientToServer = os.fdopen(rClientToServer, 'rb', 0), os.fdopen(wClientToServer, 'wb', 0)  # flujos de lectura y escritura desde cliente a servidor
frServerToClient, fwServerToClient = os.fdopen(rServerToClient, 'rb', 0), os.fdopen(wServerToClient, 'wb', 0)  # flujos de lectura y escritura desde servidor a cliente

pid = os.fork()

if pid > 0:
    #this is the client process
    frClientToServer.close()
    path = input("introduce el path del fichero: ")
    fwClientToServer.write(path.encode('utf8'))
    fwClientToServer.close()
    fwServerToClient.close()

    while True:
        data = frServerToClient.readline()
        if not data: 
            break
        data2 = data.decode('utf8')
        print("cliente recibe: " + data2)

else:
    #this is the server process
    fwClientToServer.close()

    path = frClientToServer.readline()
    print(path)
    file = open(path, "r")
    #print("el fichero sigue abierto")

    for line in file.readlines():
        fwServerToClient.write(line.encode('utf8'))

    file.close()
    print("el servidor ha terminado de enviar todas las lineas del fichero")

    frServerToClient.close()

