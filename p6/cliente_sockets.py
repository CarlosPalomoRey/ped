import socket
from time import sleep


def cliente():
    #tomar variables de la entrada de usuario
    def pedir_cometido():
        c = str(input("Cometido (1: Detener servidor, 2: Pedir hora): "))
        if c not in ['1', '2']:
            print('Cometido incorrecto, introduzca (1) o (2) para usar el cometido deseado')
            c = pedir_cometido()
        return c


    repeticiones = 3
    while repeticiones != 0:
        cometido = pedir_cometido()
        st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = 'localhost'
        port = 1234
        st.connect((host, port))
        if cometido == '1':
            st.send(bytes('Detener', "UTF-8"))
            st.close()
            break
        if cometido == '2':
            st.send(bytes('Dame la hora', "UTF-8"))
        leer = st.recv(30)
        print(f'Fecha y hora confirmada: {leer.decode("utf-8")}')
        st.close()
        repeticiones -= 1

cliente()