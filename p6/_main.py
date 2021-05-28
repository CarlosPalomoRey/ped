import cliente_file as cli
import servidor_file as serv

opcion = str(input("introduzca (1) para ejecutar cliente o (2) para ejecutar servidor "))
if opcion == '1':
    cli.cliente()
elif opcion == '2':
    print('Eligió ejecutar servidor')
    serv.servidor()
else:
    print('Error en la introducción de datos')