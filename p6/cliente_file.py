import socket

mensaje_detener_servidor = 'Detener'

def cliente():
    ruta_socket = str(input("Ruta Socket: "))

    repeticiones = 3
    while repeticiones != 0:
        # Pido al cliente que quiere hacer
        cometido = pedir_cometido()
        st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = 'localhost'
        port = 1234
        st.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        st.connect((host, port))
        # obtengo detener o ruta del fichero
        mensaje = procesar_cometido(cometido, ruta_socket)
        st.send(mensaje.encode('utf-8'))
        # Recibo datos
        st.settimeout(3)
        # comprobar_datos_recibidos(leer)
        recibir_datos(st)
        st.close()
        repeticiones -= 1


def pedir_cometido():
    c = str(input("Cometido (1: Detener servidor, 2: Pedir fichero): "))
    if c not in ['1', '2']:
        print('Cometido incorrecto, introduzca (1) o (2) para usar el cometido deseado')
        c = pedir_cometido()
    return c



def procesar_cometido(cometido, ruta):
    if cometido == '1':
        mensaje = mensaje_detener_servidor
    elif cometido == '2':
        mensaje = ruta
    else:
        raise CometidoError("Error: Cometido incorrecto")
    return mensaje

def recibir_datos(st):
    while True:
        leer = st.recv(512)  # lee el send del servidor después de mandar el contenido del servidor
        if len(leer) >0 and leer.decode("utf-8") != 'Fin':
            print(f'Contenido recibido: {leer.decode("utf-8")}')  # escribe el contenido
        else:
            print('saliendo')
            break






class CometidoError(Exception):
    pass
