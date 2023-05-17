import socket
import select

codificacion = 'utf-8'
dirServer = (str(socket.INADDR_ANY), 3000)

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketServer.bind(dirServer)
socketServer.listen(0)

sockets = [socketServer]
userSockets = dict()
usernames = []


def readSocket(sock): #funcion simple para leer un socket
    try:
        data = sock.recv(1024, 0)
        return data.decode(codificacion)
    except:
        return False

def broadcastMessage(msg, senderSocket): #Envia un mensaje a todos los sockets excepto al que escribio el mensaje y al servidor mismo
    for sock in sockets:
        if sock != senderSocket and sock != socketServer:
            username = userSockets[senderSocket]
            data = (username + ": " + msg).encode(codificacion)
            length = (f"{len(data):<10}").encode(codificacion) #Se codifica la longitud del mensaje que se va a enviar, en 10 caracteres
            sock.send(length)
            sock.send(data)
            
def newClient(socketClient):
    username = readSocket(socketClient)
    if not username: # No se pudo leer el socket
        removeClient(socketClient)
        return False
    elif username in usernames: # Comprobar que el nombre de usuario no está siendo utilizado
        error = "Este nombre de usuario no está disponible. Seleccione otro."
        socketClient.send(error.encode(codificacion))
        return False
    else: #Todo correcto, se registra el usuario y socket
        userSockets[socketClient] = username
        usernames.append(username)
        return True

def removeClient(socketClient): #borra un socket de los usuarios/sockets registrados
    sockets.remove(socketClient)
    if socketClient in userSockets:
        print("Se desconecto el usuario "+userSockets[socketClient])
        usernames.remove(userSockets[socketClient])
        del userSockets[socketClient]


while True:
    socketsToRead, _, badSockets = select.select(sockets, [], sockets)
    for sock in socketsToRead:
        if sock == socketServer:
            socketClient, dirClient = socketServer.accept()
            #Pone el socket en la lista de lectura para luego poder leer el nombre de usuario
            sockets.append(socketClient)
            
        elif not sock in userSockets: #Socket no registrado con usuario, recibe los datos del cliente (nombre de usuario) hasta que de uno valido
            success = newClient(sock)
            if success:
                # El nombre de usuario es aceptado por el servidor
                username = userSockets[sock]
                print("Se ha conectado el usuario " + username)
                mensaje = "ACK"
                sock.send(mensaje.encode(codificacion))
        else: #el socket no es el del servidor, pero si esta registrado como usuario, tiene que ser un mensaje
            # Imprimir mensaje de cliente

            msg = readSocket(sock)
            if msg:
                username = userSockets[sock]
                print(username + ": " + msg)
                broadcastMessage(msg, sock)
            else:
                removeClient(sock)