import socket

codificacion = "utf-8"
dirServer = (str(socket.INADDR_ANY), 3000)

socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
socketClient.connect(dirServer)

# Enviar al servidor un nombre de usuario no nulo
nombreUsuario = input("Introduzca un nombre de usuario para unirse al chat: ")
while not nombreUsuario:
    nombreUsuario = input("Nombre de usuario inválido. Introduzca otro para unirse al chat")
socketClient.send(nombreUsuario.encode(codificacion))

# Recibir confirmación del servidor de que el nombre de usuario el válido
while True: 
    datos = socketClient.recv(1024)
    mensaje = datos.decode(codificacion)
    print(mensaje)
    if mensaje == "Este nombre de usuario no está disponible. Seleccione otro.":
        nombreUsuario = input("Introduzca un nombre de usuario para unirse al chat: ")
        while not nombreUsuario:
            nombreUsuario = input("Nombre de usuario inválido. Introduzca otro para unirse al chat")
        socketClient.send(nombreUsuario.encode(codificacion))
    elif mensaje == "ACK":
        break
# Enviar mensajes al servidor
while True:   
    contenido = input("Introduzca un mensaje para el chat: ")
    socketClient.send(contenido.encode(codificacion))

