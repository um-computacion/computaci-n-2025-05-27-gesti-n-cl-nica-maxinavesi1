import unittest
from modelo.paciente import Paciente
from modelo.excepciones import DatosInvalidosException

class TestPaciente(unittest.TestCase):

    def test_creacion_valida(self):
        paciente = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertEqual(str(paciente), "Juan Pérez, 12345678, 12/12/2000")

    def test_datos_faltantes(self):
        with self.assertRaises(DatosInvalidosException):
            Paciente("", "12345678", "12/12/2000")
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Pérez", "", "12/12/2000")
        with self.assertRaises(DatosInvalidosException):
            Paciente("Juan Pérez", "12345678", "")
