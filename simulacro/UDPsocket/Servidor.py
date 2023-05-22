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


# import socket
# from Manejador import *

# class Servidor: 
#     dirServidor = (str(socket.INADDR_ANY), 4000)
#     codificacion = "UTF-8"

#     sockServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sockServidor.bind(dirServidor)

#     while True: 
#         sockServidor.listen(0)
#         sockServidorCliente, dirCliente = sockServidor.accept()
#         datos = sockServidorCliente.recv(1024, 0)
#         mensaje = datos.decode(codificacion)
#         print(mensaje)
#         manejador = Manejador()
#         respuesta = manejador.devolver_respuesta()
#         sockServidorCliente.send(respuesta.encode(codificacion), 0)