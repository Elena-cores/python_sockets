import socket

codificacion = 'utf-8'
nombresUsuarioRegistrados = ['patricia']
dirServer = (str(socket.INADDR_ANY), 3000)

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketServer.bind(dirServer)

while True:
    # Servidor acepta peticiones de un cliente
    socketServer.listen(0)
    socketServerClient, dirClient = socketServer.accept()
    # Recibe los datos del cliente (nombre de usuario)
    datos = socketServerClient.recv(1024, 0)
    nombreUsuario = datos.decode(codificacion)
    # Comprobar que el nombre de usuario no está siendo utilizado
    while nombreUsuario in nombresUsuarioRegistrados:
        error = "Este nombre de usuario no está disponible. Seleccione otro."
        print(error)
        socketServerClient.send(error.encode(codificacion))
        datos = socketServerClient.recv(1024, 0)
        nombreUsuario = datos.decode(codificacion)
    # El nombre de usuario es aceptado por el servidor
    nombresUsuarioRegistrados.append(nombreUsuario)
    print("Se ha conectado el usuario " + nombreUsuario)
    mensaje = "ACK"
    socketServerClient.send(mensaje.encode(codificacion))
    # Imprimir mensaje de cliente
    while True:
        datos = socketServerClient.recv(1024, 0)
        contenido = datos.decode(codificacion)
        print(nombreUsuario + " ha escrito " + contenido)
