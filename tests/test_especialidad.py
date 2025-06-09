import unittest
from modelo.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):

    def test_creacion_valida(self):
        esp = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])
        self.assertEqual(esp.obtener_especialidad(), "Pediatría")
        self.assertTrue(esp.verificar_dia("Lunes"))
        self.assertFalse(esp.verificar_dia("domingo"))
        self.assertIn("lunes", str(esp))

    def test_creacion_invalida(self):
        with self.assertRaises(ValueError):
            Especialidad("", ["lunes"])
        with self.assertRaises(ValueError):
            Especialidad("Cardiología", [])
        with self.assertRaises(ValueError):
            Especialidad("Cardiología", ["lunes", 2])  # valor no string
