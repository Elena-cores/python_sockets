import socket
from Manager import *

class Servidor: 
    dirServidor = (str(socket.INADDR_ANY), 4000)
    codificacion = "UTF-8"

    sockServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockServidor.bind(dirServidor)

    while True: 
        sockServidor.listen(0)
        sockServidorCliente, dirCliente = sockServidor.accept()
        datos = sockServidorCliente.recv(1024, 0)
        mensaje = datos.decode(codificacion)
        print(mensaje)
        manejador = Manager()
        respuesta = manejador.leer_fichero(mensaje)
        sockServidorCliente.send(respuesta.encode(codificacion), 0)