import unittest
from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.clinica import Clinica
from modelo.excepciones import *

class TestClinica(unittest.TestCase):

    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.medico = Medico("Dra. Ana García", "MED123")
        self.especialidad = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(self.especialidad)

    def test_registro_paciente_medico(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.assertIn(self.paciente, self.clinica.obtener_pacientes())
        self.assertIn(self.medico, self.clinica.obtener_medicos())

    def test_paciente_duplicado(self):
        self.clinica.agregar_paciente(self.paciente)
        with self.assertRaises(DatosInvalidosException):
            self.clinica.agregar_paciente(self.paciente)

    def test_medico_duplicado(self):
        self.clinica.agregar_medico(self.medico)
        with self.assertRaises(DatosInvalidosException):
            self.clinica.agregar_medico(self.medico)

    def test_turno_valido(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        fecha = datetime(2025, 12, 1, 10, 0)  # Lunes
        self.clinica.agendar_turno("12345678", "MED123", "Pediatría", fecha)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)

    def test_turno_duplicado(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        fecha = datetime(2025, 12, 1, 10, 0)
        self.clinica.agendar_turno("12345678", "MED123", "Pediatría", fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("12345678", "MED123", "Pediatría", fecha)

    def test_turno_paciente_inexistente(self):
        self.clinica.agregar_medico(self.medico)
        fecha = datetime(2025, 12, 1, 10, 0)
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("99999999", "MED123", "Pediatría", fecha)

    def test_turno_medico_inexistente(self):
        self.clinica.agregar_paciente(self.paciente)
        fecha = datetime(2025, 12, 1, 10, 0)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "XYZ", "Pediatría", fecha)

    def test_turno_especialidad_incorrecta(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        fecha = datetime(2025, 12, 1, 10, 0)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "MED123", "Cardiología", fecha)

    def test_emitir_receta_valida(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.clinica.emitir_receta("12345678", "MED123", ["Paracetamol"])
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_emitir_receta_sin_medicamentos(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("12345678", "MED123", [])

    def test_obtener_historia_paciente_no_existente(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.obtener_historia_clinica("99999999")
