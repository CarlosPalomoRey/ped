import socket

st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def servidor():
    print('Servidor levantado')
    host = 'localhost'
    port = 1234
    st.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    st.bind((host, port))
    st.listen(3)
    while True:
        nuevo_socket, nueva_ruta_socket = st.accept()
        # Recibe o detener servidor o la ruta
        #escucha, direccion_cliente = nuevo_socket.recvfrom(512)
        escucha = nuevo_socket.recv(512)
        escucha_procesada = procesar_escucha(escucha.decode("utf-8"))
        if escucha_procesada == 'Servidor detenido':
            nuevo_socket.close()
            st.close()
            print('Servidor detenido')
            break
        else:
            # abrir_ruta(escucha.decode('utf-8'), direccion_cliente)
            abrir_ruta(escucha.decode('utf-8'), nuevo_socket)
            print('Contenido enviado\n')

        nuevo_socket.close()



def procesar_escucha(escucha):
    if escucha == 'Detener':
        estado = 'Servidor detenido'
    else:
        estado = 'Enviada la ruta del fichero'
    return estado


def abrir_ruta(ruta, nuevo_socket):
    with open(ruta, 'r') as fichero:  # abre la ruta
        print('Servidor solicitado')
        while True:
            contenido_fichero = fichero.read(512)
            if contenido_fichero:
                print(contenido_fichero)
                nuevo_socket.send(bytes(contenido_fichero, "UTF-8"))  # manda el contenido
                print(f'Contenido del fichero enviado\n')
            else:
                nuevo_socket.send(bytes('Fin', "UTF-8"))
                print('saliendo')
                fichero.close()
                break


class ErrorEscucha(Exception):
    pass
