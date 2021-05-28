import os, sys, time
from datetime import datetime

rd,wd = os.pipe() # son file descriptors, no file objects
r, w  = os.fdopen(rd,'rb',0), os.fdopen(wd,'wb',0) # file objects

def lanzador():
    pid = os.fork()
    if pid: # padre
        print(f'Yo soy tu padre: {os.getpid()}')
        cliente(r, w)

    else:  # hijo
        print(f'Aqui tienes a tu hijo: {os.getpid()}')
        servidor(r, w)

def servidor(r, w):
    print("servidor")
    r.close()
    for i in range(10):
        mensaje = time.strftime("%H:%M:%S")
        #mensaje = "Hora %s\n" % i
        #mensaje = mensaje + "\n"
        w.write(mensaje.encode('utf8'))
        print("- servidor escribe: " + mensaje.strip())
        w.flush()
        time.sleep(3)

def cliente(r, w):
    print("cliente")
    w.close()
    while True:
        # hora = r.readline()
        hora_bytes = os.read(rd, 1024)
        hora = hora_bytes.decode('utf8').strip()
        if not hora:
            break
        # print("+ cliente lee: " + hora.decode('utf8').strip())
        print(f"+ cliente lee: {hora}")



lanzador()
