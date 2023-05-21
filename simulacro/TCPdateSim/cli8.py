import socket

class cli8: 
    dirServidor = (str(socket.INADDR_ANY), 8002)
    dirCliente = (str(socket.INADDR_ANY), 0)
    codificacion = "UTF-8"

    socketCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketCliente.bind(dirCliente)

    while True: 
        # case sensitive request
        peticion = input("Request (DATE or TIME): ")
        socketCliente.sendto(peticion.encode(codificacion), dirServidor)
        datos = socketCliente.recv(1024)
        respuesta = datos.decode(codificacion)
        print(respuesta)