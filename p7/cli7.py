import threading
import socket
alias = input('Elige un alias >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))


def client_receive():
    while True:
        mensaje = client.recv(1024).decode('utf-8')
        if mensaje == "Introduce tu alias:":
            client.send(alias.encode('utf-8'))
        elif mensaje == 'denegado':
            print("denegado, usuario ya existe")
            client.close()
            break
        elif mensaje == 'registrado':
            client_send()
            break
        else:
            print(mensaje, "\n")

    exit()


def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))



client_receive()