import unittest

import bolos

class TestPartida(unittest.TestCase):

    # test formato valido
    def test_partida_marcador_0(self):
        datos = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        resultado = bolos.calcular_resultado(datos)
        self.assertEqual(0, resultado)
    def test_partida_marcador_1(self):
        datos = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        resultado = bolos.calcular_resultado(datos)
        self.assertEqual(1, resultado)
    def test_partida_marcador_3(self):
        datos = [[0, 0], [0, 1], [0, 0], [0, 0], [2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        resultado = bolos.calcular_resultado(datos)
        self.assertEqual(3, resultado)
    def test_pleno(self):
        datos = [['X'], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        resultado = bolos.calcular_resultado(datos)
        self.assertEqual(10, resultado)
    def test_semipleno(self):
        datos = [[1, '/'], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        resultado = bolos.calcular_resultado(datos)
        self.assertEqual(10, resultado)
    def test_pleno_complejo(self):
        datos = [['X'], [3, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        resultado = bolos.calcular_resultado(datos)
        self.assertEqual(18, resultado)

    def test_semipleno_complejo(self):
        datos = [[1, '/'], [3, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        resultado = bolos.calcular_resultado(datos)
        self.assertEqual(17, resultado)

    # test formato NO valido
    def test_tirada_extra(self):
        datos = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],[0, 0],  [0, 0], ['X', 1,0]]
        with self.assertRaises(bolos.FormatError):
            resultado = bolos.calcular_resultado(datos)
    def test_pleno_mal(self):
        datos = [[3, 'X'], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        with self.assertRaises(bolos.FormatError):
            resultado = bolos.calcular_resultado(datos)
    def test_semipleno_mal(self):
        datos = [['/', 3], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        with self.assertRaises(bolos.FormatError):
            resultado = bolos.calcular_resultado(datos)
    def test_mas_10_puntos(self):
        datos = [['X', 3], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        with self.assertRaises(bolos.SintaxError):
            resultado = bolos.calcular_resultado(datos)
    def test_tres_tiradasl(self):
        datos = [[3, 2, 3], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        with self.assertRaises(bolos.FormatError):
            resultado = bolos.calcular_resultado(datos)
    def test_semipleno_pleno(self):
        datos = [['X', '/'], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        with self.assertRaises(bolos.SintaxError):
            resultado = bolos.calcular_resultado(datos)

    def test_jugadas_extra_ilegal(self):
        datos = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [2, 0], [3, 1]]
        with self.assertRaises(bolos.ValorError):
            resultado = bolos.calcular_resultado(datos)
    def test_9_JUGADAS(self):
        datos = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        with self.assertRaises(bolos.FormatError):
            resultado = bolos.calcular_resultado(datos)
    def test_no_pleno_no_jugada11(self):
        datos = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],[1,0],[2,0]]
        with self.assertRaises(bolos.FormatError):
            resultado = bolos.calcular_resultado(datos)
    def test_jugada_tres_lanzamientos(self):
        datos = [[1, 0], [0, 0], [0, 0], [0, 0,2], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],[1,0]]
        with self.assertRaises(bolos.FormatError):
            resultado = bolos.calcular_resultado(datos)
    def test_1tiro_tras_pleno10(self):
        datos = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],['X',0],[1]]
        with self.assertRaises(bolos.FormatError):
            resultado = bolos.calcular_resultado(datos)
    def test_2tiros_tras_semipleno10(self):
        datos = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],[1,'/'],[2,4]]
        with self.assertRaises(bolos.FormatError):
            resultado = bolos.calcular_resultado(datos)
    def test_1_tiro_solo(self):
        datos = [[1, 0], [5], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],[1,0]]
        with self.assertRaises(bolos.FormatError):
            resultado = bolos.calcular_resultado(datos)

    #al parecer no vale con sintaxerror es un FormatError
    def test_pleno_ilegal_con_numero(self):
        datos = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], ['X', 4], [0, 0], [0, 0], [0, 0],[1,0]]
        with self.assertRaises(bolos.FormatError):
            resultado = bolos.calcular_resultado(datos)
    def test_pleno_ilegal_con_semi(self):
        datos = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], ['X', '/'], [0, 0], [0, 0], [0, 0],[1,0]]
        with self.assertRaises(bolos.FormatError):
            resultado = bolos.calcular_resultado(datos)
    def test_semipleno_ilegal_con_numero(self):
        datos = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], ['/', 3], [0, 0], [0, 0], [0, 0],[1,0]]
        with self.assertRaises(bolos.FormatError):
            resultado = bolos.calcular_resultado(datos)
    def test_pleno_ilegal_con_numero(self):
        datos = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], ['/', 'X'], [0, 0], [0, 0], [0, 0],[1,0]]
        with self.assertRaises(bolos.FormatError):
            resultado = bolos.calcular_resultado(datos)