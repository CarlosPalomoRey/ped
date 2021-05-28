import unittest
import cliente_file as cli
import servidor_file as serv


class MyTestCase(unittest.TestCase):
    def test_entrada(self):
        self.assertEqual(True, False)
    def test_cs_01(self):
        # cliente
        cometido = '1'
        mensaje = cli.procesar_cometido(cometido)
        # servidor
        escuchado = mensaje
        estado_final = serv.procesar_escucha(escuchado)
        self.assertEqual('Servidor detenido', estado_final)
    def test_cs_02(self):
        # cliente
        cometido = '2'
        mensaje = cli.procesar_cometido(cometido)
        # servidor
        escuchado = mensaje
        estado_final = serv.procesar_escucha(escuchado)
        self.assertEqual('Dame la ruta del fichero', estado_final)

    # tests cliente
    def test_cliente_01_procesar_cometido_1(self):
        cometido = '1'
        mensaje = cli.procesar_cometido(cometido)
        self.assertEqual('Detener', mensaje)
    def test_cliente_02_procesar_cometido_2(self):
        cometido = '2'
        mensaje = cli.procesar_cometido(cometido)
        self.assertEqual('Dame la ruta del fichero', mensaje)
    def test_cliente_03_procesar_cometido_x(self):
        cometido = 'x'
        with self.assertRaises(cli.CometidoError):
            mensaje = cli.procesar_cometido(cometido)

