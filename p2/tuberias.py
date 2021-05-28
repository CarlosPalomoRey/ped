import os, sys, time
rd,wd = os.pipe()
# son file descriptors, no file objects
r, w  = os.fdopen(rd,'rb',0), os.fdopen(wd,'wb',0) # file objects
pid = os.fork()
if pid: # padre
    w.close()
    while True:
        data = r.readline()
        if not data:
            break
        print("el padre lee: " + data.decode('utf8').strip())
else:  # hijo
    r.close()
    for i in range(10):
        mensaje = "linea %s\n" % i
        w.write(mensaje.encode('utf8'))
        w.flush()
        time.sleep(1)