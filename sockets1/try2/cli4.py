import socket, setproctitle

pathSocketBase = '/tmp/ped2-p'
nombreSocket = 'socket'
pathFichero = 'patricia/fichero.txt'
codificacion = "latin-1"
setproctitle.setproctitle("cli4")

# Nombre del socket
nombreSocket = input("Introduzca un nombre para el socket (por defecto socket): ") or nombreSocket

# Introduce el path a un fichero o que pare el servidor
entradaDatos = input("Introduzca un path a un fichero (o `" + pathFichero + "` por defecto): ") or pathFichero

# Crea el socket y se conecta 
socketObj = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)
pathSocketCompleto = pathSocketBase + nombreSocket
#socketObj.bind(path)
socketObj.connect(pathSocketCompleto)
# Envía la ruta del path al servidor
print("El cliente ha enviado estos datos: " + entradaDatos)
socketObj.send(entradaDatos.encode(codificacion), 0)
# Lee el contenido enviado por el servidor y lo muestra
contenidoFinal = ''
while True:
    datos = socketObj.recv(1024).decode(codificacion)
    if not datos:
        break
    contenidoFinal += datos
    print(datos)
print("El cliente ha recibido: " + contenidoFinal)
# Cierra la conexión
# socketObj.shutdown(socket.SHUT_RD)
