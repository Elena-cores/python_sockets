import socket
from Manage import *

class Servidor: 
    dirServidor = (str(socket.INADDR_ANY), 4000)
    codificacion = "UTF-8"

    sockServidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockServidor.bind(dirServidor)

    while True: 
        datos, dirCliente = sockServidor.recvfrom(1024)
        mensaje = datos.decode(codificacion)
        print(mensaje)
        manejador = Manage()
        respuesta = manejador.devolver_respuesta()
        sockServidor.sendto(respuesta.encode(codificacion), dirCliente)