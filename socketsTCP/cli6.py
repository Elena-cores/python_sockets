import socket, setproctitle, sys

pathFichero = 'patricia/fichero.txt'
codificacion = "UTF-8"
puertoServidor = 2221

setproctitle.setproctitle("cli6")

# Crear el socket
socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Obtener la dirección IP y el puerto del socket
ip, puerto = socketObj.getsockname()
print("La IP del socket UDP es " + str(ip) + " y su puerto es " + str(puerto), file=sys.stderr)
# Personalización del puerto
puertoPersonalizado = input("Introduzca el puerto del servidor con 4 dígitos (por defecto: 2221):") or puertoServidor
while (len(str(puertoPersonalizado)) != 4 or not str(puertoPersonalizado).isdigit()):
    puertoPersonalizado = input("Valor inválido. Introduzca el puerto del servidor (por defecto: 2221):") or puertoServidor
# Introduce el path a un fichero o que pare el servidor
entradaDatos = input("Introduzca un path a un fichero (o `" + pathFichero + "` por defecto): ") or pathFichero
# Se conecta al servidor
socketObj.connect((str(socket.INADDR_ANY), int(puertoPersonalizado)))
# Envía la ruta del path al servidor
print("El cliente ha enviado estos datos: " + entradaDatos, file=sys.stderr)
socketObj.send(entradaDatos.encode(codificacion), 0)
# Lee el contenido enviado por el servidor y lo muestra
contenidoFinal = b''
while True:
    datos = socketObj.recv(1024)
    if not datos:
        break
    contenidoFinal += datos
    # print(datos)
# print("El cliente ha recibido: " + contenidoFinal, file=sys.stderr)
# Utilizar el encoding correcto
try: 
    print(contenidoFinal.decode(codificacion))
except: 
    print(contenidoFinal)