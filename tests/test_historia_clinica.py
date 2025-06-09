import unittest
from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.turno import Turno
from modelo.receta import Receta
from modelo.historia_clinica import HistoriaClinica

class TestHistoriaClinica(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.medico = Medico("Dra. Ana García", "MED123")
        self.medico.agregar_especialidad(Especialidad("Pediatría", ["lunes"]))
        self.historia = HistoriaClinica(self.paciente)

    def test_agregar_turno(self):
        turno = Turno(self.paciente, self.medico, datetime(2025, 12, 1, 10, 0), "Pediatría")
        self.historia.agregar_turno(turno)
        self.assertIn(turno, self.historia.obtener_turnos())

    def test_agregar_receta(self):
        receta = Receta(self.paciente, self.medico, ["Ibuprofeno"])
        self.historia.agregar_receta(receta)
        self.assertIn(receta, self.historia.obtener_recetas())

    def test_str_historia(self):
        turno = Turno(self.paciente, self.medico, datetime(2025, 12, 1, 10, 0), "Pediatría")
        receta = Receta(self.paciente, self.medico, ["Ibuprofeno"])
        self.historia.agregar_turno(turno)
        self.historia.agregar_receta(receta)
        texto = str(self.historia)
        self.assertIn("Juan Pérez", texto)
        self.assertIn("Ibuprofeno", texto)
        self.assertIn("Pediatría", texto)
