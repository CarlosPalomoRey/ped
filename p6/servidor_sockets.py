import socket
import time
from _socket import SHUT_RDWR

st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# interrupcion = False
def servidor():
    print('Servidor levantado')
    host = 'localhost'
    port = 1234
    st.bind((host,port))
    st.listen(3)

    while True:
        nuevo_socket, nueva_ruta_socket = st.accept()
        escucha = nuevo_socket.recv(30)
        if escucha == b'Detener':
            nuevo_socket.close()
            st.close()
            print('Servidor detenido')
            break
        else:
            nuevo_socket.send(bytes(time.strftime("Fecha: %d/%m/%Y - %H:%M:%S"), "UTF-8"))
            print('Fecha y hora enviada\n')
        nuevo_socket.close()



servidor()

