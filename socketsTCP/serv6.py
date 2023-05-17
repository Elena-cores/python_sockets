import socket, setproctitle, signal

codificacion = "UTF-8"
puertoServidor = 2221

setproctitle.setproctitle("serv6")

# Creación del socket
socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Personalización del puerto
puertoPersonalizado = input("Introduzca el puerto para el servidor con 4 dígitos (por defecto: 2221):") or puertoServidor
while (len(str(puertoPersonalizado)) != 4 or not str(puertoPersonalizado).isdigit()):
    puertoPersonalizado = input("Valor inválido. Introduzca el puerto para el servidor (por defecto: 2221):") or puertoServidor
socketObj.bind((str(socket.INADDR_ANY), int(puertoPersonalizado)))

# Obtener la dirección IP y el puerto del socket
ipActual, puertoActual = socketObj.getsockname()
print("La IP del socket UDP es " + str(ipActual) + " y su puerto es " + str(puertoActual))

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
    socketCliente, direccionCliente = socketObj.accept()
    datosCliente = socketCliente.recv(10000, 0).decode(codificacion)
    # Recibe la petición de parar del cliente
    if datosCliente == "stop":
        mensaje = "Servidor parando a petición del cliente"
        print(mensaje)
        socketCliente.send(mensaje.encode(codificacion), 0)
        socketCliente.shutdown(socket.SHUT_RD)
        # socketObj.close()
        break
    # Recibe el path del fichero desde el cliente
    else: 
        pathFichero = datosCliente
        print("El servidor ha recibido estos datos: " + pathFichero)
        # Lee el contenido del fichero, especificando la codificación
        try:
            with open(pathFichero, 'rb') as fichero:
                contenido = fichero.read()
        # No encuentra el fichero con ese path
        except:
            error = "'Error: no se ha encontrado el fichero en el path especificado'"
            print(error)
            socketCliente.send(error.encode(codificacion), 0)
            socketCliente.close()
        else:
            # El archivo tiene contenido
            if contenido != b"":
                print("El servidor ha leído el contenido del fichero " + pathFichero + " correctamente")
                # Envía el contenido del fichero al cliente
                socketCliente.send(contenido)
                # Cierra el socket porque si no en bucle infinito
                # socket2Obj.shutdown(socket.SHUT_RD)
                socketCliente.close()
            # El archivo está vacío 
            else:
                print("Este fichero no tiene contenido: " + pathFichero)
                error = "'Error: el archivo no tiene contenido'"
                socketCliente.send(error.encode(codificacion), 0)
                socketCliente.close()
