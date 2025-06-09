import unittest
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.excepciones import DatosInvalidosException

class TestMedico(unittest.TestCase):

    def setUp(self):
        self.medico = Medico("Dra. Ana García", "MED123")
        self.pediatria = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.cardiologia = Especialidad("Cardiología", ["martes"])

    def test_creacion_valida(self):
        self.assertEqual(self.medico.obtener_matricula(), "MED123")

    def test_agregar_especialidad_valida(self):
        self.medico.agregar_especialidad(self.pediatria)
        self.assertEqual(self.medico.obtener_especialidad_para_dia("lunes"), "Pediatría")

    def test_especialidad_duplicada(self):
        self.medico.agregar_especialidad(self.pediatria)
        with self.assertRaises(DatosInvalidosException):
            self.medico.agregar_especialidad(self.pediatria)

    def test_especialidad_no_disponible(self):
        self.medico.agregar_especialidad(self.cardiologia)
        self.assertIsNone(self.medico.obtener_especialidad_para_dia("jueves"))

    def test_creacion_invalida(self):
        with self.assertRaises(DatosInvalidosException):
            Medico("", "MED123")
        with self.assertRaises(DatosInvalidosException):
            Medico("Dra. Ana", "")
