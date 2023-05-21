import socket

class Cliente: 
    dirServidor = (str(socket.INADDR_ANY), 4000)
    dirCliente = (str(socket.INADDR_ANY), 0)
    codificacion = "UTF-8"

    sockCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockCliente.bind(dirCliente)
    
    sockCliente.sendto("Hola Servidor".encode(codificacion), dirServidor)
    datos, dirServidor= sockCliente.recvfrom(1024)
    mensaje = datos.decode(codificacion)
    print(mensaje)