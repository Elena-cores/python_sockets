import os, socket, setproctitle, signal

pathSocketBase = '/tmp/ped2-p'
nombreSocket = 'socket'
codificacion = "latin-1"
setproctitle.setproctitle("serv4")

# crear el socket y asociarlo al path
nombreSocket = input("Introduzca un nombre para el socket (por defecto socket): ") or nombreSocket
pathSocketCompleto = pathSocketBase + nombreSocket

# borrar el socket cuando finaliza el servidor
if os.path.exists(pathSocketBase + nombreSocket):
    os.remove(pathSocketBase + nombreSocket)

print("Se ha creado en socket en: " + pathSocketCompleto)
socketObj = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)
socketObj.bind(pathSocketCompleto)

# Parar el servidor desde el propio servidor
def manejadorSennal(sig, frame):
    mensaje = "Servidor parando"
    print(mensaje)
    socketObj.shutdown(socket.SHUT_RD)
    exit(0)

signal.signal(signal.SIGINT, manejadorSennal)

while True: 
    # El socket principal escucha y acepta la petición creando otro socket
    socketObj.listen(0)
    socket2Obj, direccion = socketObj.accept()
    datosCliente = socket2Obj.recv(10000, 0).decode(codificacion)
    # Recibe la petición de parar del cliente
    if datosCliente == "stop":
        mensaje = "Servidor parando a petición del cliente"
        print(mensaje)
        socket2Obj.send(mensaje.encode(codificacion), 0)
        socket2Obj.shutdown(socket.SHUT_RD)
        # socketObj.close()
        break
    # Recibe el path del fichero desde el cliente
    else: 
        pathFichero = datosCliente
        print("El servidor ha recibido estos datos: " + pathFichero)
        # Lee el contenido del fichero, especificando la codificación
        try:
            with open(pathFichero, 'r', encoding=codificacion) as fichero:
                contenido = fichero.read()
        # No encuentra el fichero con ese path
        except:
            error = "'Error: no se ha encontrado el fichero en el path especificado'"
            print(error)
            socket2Obj.send(error.encode(codificacion), 0)
            socket2Obj.close()
        else:
            # El archivo tiene contenido
            if contenido != "":
                print("El servidor ha leído el contenido del fichero " + pathFichero + " correctamente")
                # Envía el contenido del fichero al cliente
                socket2Obj.send(contenido.encode(codificacion), 0)
                # Cierra el socket porque si no en bucle infinito
                # socket2Obj.shutdown(socket.SHUT_RD)
                socket2Obj.close()
            # El archivo está vacío 
            else:
                print("Este fichero no tiene contenido: " + pathFichero)
                error = "'Error: el archivo no tiene contenido'"
                socket2Obj.send(error.encode(codificacion), 0)
                socket2Obj.close()