import os, time, sys
import psutil

nombre_fifo_C_S = 'fifo_C_S'
nombre_fifo_S_C = 'fifo_S_C'


# problema de interbloqueo, alternancia de read y write mal hecha
def cliente():
    # Envia el nombre de un fichero y recibe su contenido (y lo imprime)
    print("+ [cliente] iniciado")

    # En fifo_A envia el nombre del fichero para que lo lea el servidor
    c_s_escritura = os.open(nombre_fifo_C_S, os.O_WRONLY)
    # ruta_fichero = 'fichero-prueba.txt\n'
    ruta_fichero = 'genesis.txt'
    os.write(c_s_escritura, ruta_fichero.encode('utf8'))
    print("+ [cliente] escribe ruta")
    os.close(c_s_escritura)

    s_c_lectura = open(nombre_fifo_S_C, 'r')
    while True:
        texto = s_c_lectura.readline()[:-1] # para no leer el salto de linea
        # print("+ [cliente] entra en while de lectura (s-c)")
        if not texto:
            break
        print(f'+ [cliente] Texto recibido: {texto}')

    # print("- [cliente] termina")
    s_c_lectura.close()



def servidor():
    print("- [servidor] iniciado")
    c_s_lectura = open(nombre_fifo_C_S, 'r')
    ruta = c_s_lectura.readline()
    print(f'- [servidor] recibe la ruta ruta (c_s): [{ruta}]')
    fichero = open(ruta, 'r')
    c_s_lectura.close()

    # Existen dos posibilidades (se usa la 2 por mayor coherencia):
    # 1) while_c_lee_al_final() hace que el servidor escriba en el fifo hasta que pare
    # y finalmente el cliente lee la totalidad del contenido
    # 2) while_intercalando_c_s() hace que el servidor vaya escribiendo y parando de escribir a cada línea
    # haceiendo que a cada línea escrita o cada varias (según el sleep) el cliente lo lea del fifo

    def while_intercalando_c_s():
        while True:
            s_c_escritura = os.open(nombre_fifo_S_C, os.O_WRONLY)
            time.sleep(1)
            # print("- [servidor] entra en WHILE")
            texto_fichero = fichero.readline()[:]
            if not texto_fichero:
                break
            os.write(s_c_escritura, texto_fichero.encode('utf8'))
            # print(f'- [servidor] escribe (s-c): [{texto_fichero}]')
            os.close(s_c_escritura)
        os.close(s_c_escritura)
        # print("- [servidor] termina")

    def while_c_lee_al_final():
        s_c_escritura = os.open(nombre_fifo_S_C, os.O_WRONLY)
        while True:
            # time.sleep(1)
            print("- [servidor] entra en WHILE")
            texto_fichero = fichero.readline()[:]
            if not texto_fichero:
                break
            os.write(s_c_escritura, texto_fichero.encode('utf8'))
            print(f'- [servidor] escribe (s-c): [{texto_fichero}]')

        os.close(s_c_escritura)
        print("- [servidor] termina")

    while_intercalando_c_s()



if os.path.exists(nombre_fifo_C_S):
    os.unlink(nombre_fifo_C_S)

if os.path.exists(nombre_fifo_S_C):
    os.unlink(nombre_fifo_S_C)

os.mkfifo(nombre_fifo_C_S)
os.mkfifo(nombre_fifo_S_C)

if os.fork() == 0:
    cliente()
else:
    servidor()

'''
# The PID ID of the process needed
    pid_id = 1216
    # Informations of the Process with the PID ID
    process_pid = psutil.Process(pid_id)
    print(process_pid)
    # Gives You PID ID, name and started date
    # psutil.Process(pid=1216, name='ATKOSD2.exe', started='21:38:05')
    # Name of the process
    process_name = process_pid.name()
'''
