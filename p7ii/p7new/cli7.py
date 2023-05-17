import socket, select, sys

codificacion = "utf-8"
dirServer = (str(socket.INADDR_ANY), 3000)


# Enviar al servidor un nombre de usuario no nulo
nombreUsuario = input("Introduzca un nombre de usuario para unirse al chat: ")
while not nombreUsuario:
    nombreUsuario = input("Nombre de usuario inválido. Introduzca otro para unirse al chat")

socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
socketClient.connect(dirServer)
socketClient.setblocking(False)

socketClient.send(nombreUsuario.encode(codificacion))

# Recibir confirmación del servidor de que el nombre de usuario el válido
while True: 
    try:
        datos = socketClient.recv(1024)
        mensaje = datos.decode(codificacion)
        print(mensaje)
        if mensaje == "Este nombre de usuario no está disponible. Seleccione otro.":
            nombreUsuario = input("Introduzca un nombre de usuario para unirse al chat: ")
            while not nombreUsuario:
                nombreUsuario = input("Nombre de usuario inválido. Introduzca otro para unirse al chat: ")
            socketClient.send(nombreUsuario.encode(codificacion))
        elif mensaje == "ACK":
            break
    except:
        continue

# Escuchar del servidor o de la entrada estándar
while True:   
    inputs, _, badInputs = select.select([socketClient, sys.stdin], [], [socketClient, sys.stdin])
    for i in inputs:
        if i == socketClient:
            msgLength = socketClient.recv(10, 0) #Para leer mensaje por mensaje, el servidor envia la longitud primero y luego el mensaje
            msgLength = msgLength.decode(codificacion)
            msgLength = msgLength.replace(' ', '')
            if msgLength:
                size = int(msgLength)
                receivedMsg = socketClient.recv(size, 0)
                receivedMsg = receivedMsg.decode(codificacion)
                print(receivedMsg)
        elif i == sys.stdin:
            msg = None
            for line in sys.stdin:
                msg = line.rstrip()
                break
            sys.stdin.flush()
            
            if msg:
                socketClient.send(msg.encode(codificacion))


