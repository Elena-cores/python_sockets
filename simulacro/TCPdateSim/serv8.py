import socket
from TCPdateSim.Alerts import *

class serv8: 
    dirServidor = (str(socket.INADDR_ANY), 8002)
    encoding = "UTF-8"

    socketServidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketServidor.bind(dirServidor)

    while True:
        datos, dirCliente = socketServidor.recvfrom(1024, 0)
        peticion = datos.decode(encoding)
        print("Message received: " + peticion)
        mensaje = Alerts(peticion)
        respuesta = str(mensaje.devolver_respuesta())
        print("Response: " + respuesta)
        socketServidor.sendto(respuesta.encode(encoding), dirCliente)