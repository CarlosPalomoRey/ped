import os, time, sys
nombre_fifo_A = 'fifo-A'
FIFOA = '/tmp/nombre_fifoA'
FIFOB = '/tmp/nombre_fifoB'
if os.path.exists(FIFOA):
    os.unlink(FIFOA)
os.mkfifo(FIFOA)
if os.path.exists(FIFOB):
    os.unlink(FIFOB)
os.mkfifo(FIFOB)

def cliente():
    print("entra en cliente")
    # Abrimos el fifo
    fd = os.open(FIFOA, os.O_WRONLY)
    ruta_fichero = '/etc/services'
    # Enviamos la ruta
    os.write(fd, ruta_fichero.encode('utf8'))
    # Cerramos fifo
    os.close(fd)
    # Recibo el contenido enviado por el servidor. Se queda esperando hasta que se abra el fifob
    with open(FIFOB, "r") as file:
        print('Fifo abierta')
        # obtengo lo enviado por el cliente
        buffer = file.read()
    # Imprimo el contenido
    print(buffer)
    # cerramos fichero
    file.close()




def servidor():
    print("entra en servidor")
    # abro el fifo
    with open(FIFOA, "r") as file:
        print('Fifo abierta')
        # obtengo lo enviado por el cliente
        buffer = file.read()
    # abro la ruta que me envía el cliente
    fichero = open(buffer, 'r')
    # Leo el contenido del fichero
    data = fichero.read()
    print("escribe B:")
    #cerramos fichero
    file.close()
    # Abro la fifo B puesto que las fifo son unidireccionales
    fd1 = os.open(FIFOB, os.O_WRONLY)
    # Envío el contenido
    os.write(fd1, data.encode('utf8'))
    # Cerramos fifo
    os.close(fd1)

if os.fork() == 0:
    cliente()
else:
    servidor()
