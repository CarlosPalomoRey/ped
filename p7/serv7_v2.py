import threading
import socket
import sys
import os, select, time

host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen()
clients = []
aliases = []
diccionario_aliases = {}


def broadcast(message):
    for client in clients:
        client.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message.decode('utf-8') == "/salir":
                index = clients.index(client)
                clients.remove(client)
                client.close()
                alias = aliases[index]
                broadcast(f'\n{alias} ha abandonado el chat\n'.encode('utf-8'))
                aliases.remove(alias)
                break
            else:
                broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'\n{alias} ha abandonado el chat\n'.encode('utf-8'))
            aliases.remove(alias)
            break


def pedir_alias(cliente):
    cliente.send('Introduce tu alias:'.encode('utf-8'))
    alias = cliente.recv(1024).decode('utf-8')
    if alias != 'cancelar':
        if alias in diccionario_aliases.values():
            alias = pedir_alias(cliente)
        else:
            cliente.send('registrado'.encode('utf-8'))
            ok = cliente.recv(1024)
            print('El nuevo cliente se ha registrado ')

    return alias


def receive():
    print('Servidor iniciado')
    lista_sockets = [server]
    while True:
        lista_ready, _, _ = select.select(lista_sockets, [], [])
        for fd in lista_ready:
            if fd == server:
                # import pdb; pdb.set_trace()
                # print(f"nueva conexion en fd = {fd.fileno()}")
                cliente, _ = server.accept()
                lista_sockets.append(cliente)
                clients.append(cliente)
                alias = pedir_alias(cliente)
                print('Nuevo usuario:', alias)
                diccionario_aliases[cliente.fileno()] = alias
                broadcast(f'{alias} se ha conectado al chat'.encode('utf-8'))
            else:
                data = fd.recv(1024)
                if not data:
                    # cierre abrupto de cliente
                    lista_sockets.remove(fd)
                    clients.remove(fd)
                    del diccionario_aliases[fd.fileno()]
                    fd.close()
                else:
                    # hay datos: chateamos
                    broadcast(f"{data}\n".encode('utf8'))


if __name__ == "__main__":
    receive()
