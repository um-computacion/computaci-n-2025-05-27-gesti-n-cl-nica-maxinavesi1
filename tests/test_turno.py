import unittest
from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.turno import Turno
from modelo.especialidad import Especialidad

class TestTurno(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.medico = Medico("Dra. Ana García", "MED123")
        self.medico.agregar_especialidad(Especialidad("Pediatría", ["lunes"]))
        self.fecha = datetime(2025, 12, 1, 10, 0)
        self.turno = Turno(self.paciente, self.medico, self.fecha, "Pediatría")

    def test_obtener_medico_y_fecha(self):
        self.assertEqual(self.turno.obtener_medico(), self.medico)
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha)

    def test_str_representacion(self):
        texto = str(self.turno)
        self.assertIn("Juan Pérez", texto)
        self.assertIn("Dra. Ana García", texto)
        self.assertIn("2025-12-01 10:00", texto)
        self.assertIn("Pediatría", texto)
