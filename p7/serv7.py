import threading
import socket
import sys
host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((host, port))
server.listen()
clients = []
aliases = []


def broadcast(message):
    for client in clients:
        client.send(message)




def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break

def pedir_alias(cliente):
    cliente.send('Introduce tu alias:'.encode('utf-8'))
    alias = cliente.recv(1024).decode('utf-8')
    # TODO: hacer un select para que no se quede esperando
    if alias in aliases:
        cliente.send('denegado'.encode('utf-8'))
        #cliente.close()
        # kill(cliente)
        #sys.exit()
        # pedir_alias(cliente)

    else:
        cliente.send('registrado'.encode('utf-8'))
        print('El nuevo cliente se ha registrado ')
        aliases.append(alias)
        clients.append(cliente)
        return alias


def receive():
    while True:
        print('Server iniciado y escuchando ...')
        cliente, address = server.accept()
        print(f'Conectado con: {str(address)}')
        alias = pedir_alias(cliente)
        print(f'El Alias del cliente es: {alias}'.encode('utf-8'))
        broadcast(f'{alias} se ha conectado al chat'.encode('utf-8'))
        cliente.send('Te has conectado al chat!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(cliente,))
        thread.start()


if __name__ == "__main__":
    receive()