import os, sys, select
import threading
import socket
import time


def gestionar_registro(client):
    iteracion = 0
    while True:
        iteracion += 1
        mensaje = client.recv(1024).decode('utf-8')
        if mensaje == "Introduce tu alias:":
            if iteracion == 1:
                print('\nIntroduce tu alias o escribe "cancelar" para cancelar el registro')
                alias = input('Introduce un alias >>> ')
            else:
                print('\nAlias ya en uso, elige otro alias o escribe "cancelar" para cancelar el registro')
                alias = input('Introduce otro alias >>> ')
            client.send(alias.encode('utf-8'))
            if alias == "cancelar":
                sys.exit()
            alias_final = alias
        elif mensaje == 'registrado':
            client.send(bytes('ok', 'utf-8'))
            print('Te has conectado al chat!')
            print('Escribe "/salir" cuando quieras salir del chat')
            break
        else:
            client.send('no se que es esto'.encode('utf8'))

    return alias


def client_receive(alias, cliente):
    while True:
        mensaje = cliente.recv(1024).decode('utf-8')
        if not mensaje.startswith(alias):
            print(mensaje)



def lanzador():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 59000))
    print("cliente conectado con el servidor")

    # alias = input("dime el alias: ")
    # client.send(alias.encode('utf8'))
    # data = client.recv(1024)
    # print(f"el servidor dice {data}")

    alias = gestionar_registro(client)

    lista_sockets = [client, sys.stdin]
    print("escribe algo o el servidor nos lo mandará")
    while True:
        ready, _, _ = select.select(lista_sockets, [], [])
        for fd in ready:
            if fd == sys.stdin:
                # actividad en el teclado
                msg = str(input())
                if msg == "/salir":
                    sys.exit()
                enviar = f'{alias}: {msg}'
                client.send(enviar.encode('utf8'))
            else:
                # mensaje del servidor
                data = (client.recv(1024)).decode('utf-8')
                prefijo_propio = f'{alias}:'
                if not data.startswith(prefijo_propio):
                    print(data)
        if not ready:
            print("tiemout al canto")


lanzador()

