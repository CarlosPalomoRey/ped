
class Comprobador_de_formato(object):
    def comprobar_formato(self, entrada):
        if len(entrada) != 10 or len(entrada) != 11:
        # tiene que haber 10 o 11 jugadas
            raise FormatError("Error: Numero incorrecto de jugadas")

        else:
            for i in range(0, len(entrada)-1):
                jugada = entrada[i]
                if len(jugada) > 2:
                    # que no haya jugadas con 3+ lanzamientos
                    raise FormatError("Error: ultima tirada")

                elif len(jugada) == 1 and i != 11:
                    # salvo si es la jugada 11, y tiene solo una tirada...
                    if jugada[0] != 'X':
                    # ...tiene que ser un pleno.
                        raise FormatError("Error: Tiene que ser un pleno")

                elif len(jugada) == 2 and i != 11:
                    # salvo si es la jugada 11, y tiene dos tiradas y...
                    if jugada[0] == 'X' and jugada[1] != 0:
                        # ...si (la primera tirada) es un pleno, solo se acepta que se siga un 0
                        raise SintaxError('Error: Jugada pleno ilegal')
                    elif jugada[1] == 'X' or jugada[0] == '/':
                        # X ó / donde no deben estar
                        raise FormatError('Error: Jugada semipleno ilegal')
                    elif jugada[1] == '/' and not (jugada[0] in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
                        # ...si (la segunda tirada) forma semipleno, la primera solo puede ser un numero entre el 0 y el 9
                        raise FormatError('Error: Jugada semipleno ilegal')

                elif i == 11 and len(jugada) == 1:
                    if entrada[10][1] != '/':
                        # si hay jugada 11 con solo una tirada, tiene que tener semipleno en la 10
                        raise ValorError("Error: ultima tirada")

                elif i == 11 and len(jugada) == 2:
                    if entrada[10][0] != 'X':
                     # si hay jugada 11 con dos tiradas, tiene que tener pleno en la 10
                        raise ValorError("Error: Demasiadas jugadas")

    def assertRaisesRegex(self, ValueError, param):
        pass


def calcular_resultado(datos):

    cf = Comprobador_de_formato()
    cf.comprobar_formato(datos)

    suma = 0
    for i in range(0, len(datos)-1):
        if datos[i][0] == 'X':
            if i == 11:
                suma += 10
            else:
                suma += 10 + puntuacion_bola(i+1, 0, datos) + puntuacion_bola(i+1, 1, datos)
        
        elif datos[i][1] == '/':
            if i == 11:
                suma += 10
            else:
                suma += 10 + puntuacion_bola(i+1, 0, datos)

        else:
            suma = suma + puntuacion_bola(i, 0, datos) + puntuacion_bola(i, 1, datos)

    return suma

def puntuacion_bola(x, y, datos):
    if datos[x][y] == "X":
        return 10
    elif datos[x][y] == "/":
        return 10 - datos[x][y-1]
    else:
        return datos[x][y]

class FormatError(Exception):
    pass


class SintaxError(Exception):
    pass
class ValorError(Exception):
    pass