import os
from datetime import datetime
from time import sleep


def lanzador():
    r, w = os.pipe()
    if os.fork():
        # padre
        print(f'Yo soy tu padre: {os.getpid()}')
        if os.fork():
            # padre
            print(f'Yo soy tu padre: {os.getpid()}')
        else:
            # hijo 2
            print(f'Hijo 2 {os.getpid()}')
            servidor(r, w)

    else:
        # hijo 1
        print(f'Hijo 1 {os.getpid()}')
        cliente(r, w)


def servidor(r, w):
    os.close(r)
    print("servidor")
    write = os.fdopen(w, "w")
    while True:

        time_ahora = datetime.now()
        ahora = time_ahora.strftime("%H.%M.%S")
        write.write(ahora)
        # write.close()


def cliente(r, w):
    os.close(w)
    print("cliente")
    read = os.fdopen(r, "r")
    while True:
        ahora = read.read()
        print(ahora)
        # read.close()


lanzador()
