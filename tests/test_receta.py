import unittest
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.receta import Receta
from modelo.especialidad import Especialidad

class TestReceta(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.medico = Medico("Dra. Ana García", "MED123")
        self.medico.agregar_especialidad(Especialidad("Pediatría", ["lunes"]))

    def test_receta_valida(self):
        medicamentos = ["Ibuprofeno", "Paracetamol"]
        receta = Receta(self.paciente, self.medico, medicamentos)
        self.assertIn("Ibuprofeno", str(receta))
        self.assertIn("Juan Pérez", str(receta))

    def test_receta_vacia(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, [])

    def test_receta_medicamento_invalido(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, ["", "   "])
