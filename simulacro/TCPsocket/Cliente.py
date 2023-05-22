import socket

class Cliente: 
    dirServidor = (str(socket.INADDR_ANY), 4000)
    codificacion = "UTF-8"
    rutaDefecto = "fichero.txt"

    sockCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockCliente.connect(dirServidor)
    rutaFichero = input("Introduzca una ruta a un fichero (por defecto 'fichero.txt'): ") or rutaDefecto
    sockCliente.send(rutaFichero.encode(codificacion), 0)
    datos = sockCliente.recv(1024, 0)
    mensaje = datos.decode(codificacion)
    print(mensaje)