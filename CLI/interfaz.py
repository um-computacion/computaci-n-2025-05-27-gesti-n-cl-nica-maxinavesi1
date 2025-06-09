from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.excepciones import *

from datetime import datetime

class CLI:
    def __init__(self):
        self.__clinica = Clinica()

    def mostrar_menu(self):
        while True:
            print("\n--- Menú Clínica ---")
            print("1) Agregar paciente")
            print("2) Agregar médico")
            print("3) Agendar turno")
            print("4) Agregar especialidad a médico")
            print("5) Emitir receta")
            print("6) Ver historia clínica")
            print("7) Ver todos los turnos")
            print("8) Ver todos los pacientes")
            print("9) Ver todos los médicos")
            print("0) Salir")

            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1": self.agregar_paciente()
                case "2": self.agregar_medico()
                case "3": self.agendar_turno()
                case "4": self.agregar_especialidad()
                case "5": self.emitir_receta()
                case "6": self.ver_historia_clinica()
                case "7": self.ver_turnos()
                case "8": self.ver_pacientes()
                case "9": self.ver_medicos()
                case "0": print("Saliendo..."); break
                case _: print("Opción inválida")

    def agregar_paciente(self):
        try:
            nombre = input("Nombre: ")
            dni = input("DNI: ")
            fecha = input("Fecha de nacimiento (dd/mm/aaaa): ")
            paciente = Paciente(nombre, dni, fecha)
            self.__clinica.agregar_paciente(paciente)
            print("✅ Paciente agregado.")
        except Exception as e:
            print(f"⚠️ Error: {e}")

    def agregar_medico(self):
        try:
            nombre = input("Nombre del médico: ")
            matricula = input("Matrícula: ")
            medico = Medico(nombre, matricula)
            self.__clinica.agregar_medico(medico)
            print("✅ Médico agregado.")
        except Exception as e:
            print(f"⚠️ Error: {e}")

    def agregar_especialidad(self):
        try:
            matricula = input("Matrícula del médico: ")
            medico = self.__clinica.obtener_medico_por_matricula(matricula)
            tipo = input("Especialidad: ")
            dias = input("Días de atención (separados por coma, ej: lunes,miércoles): ").split(",")
            especialidad = Especialidad(tipo, dias)
            medico.agregar_especialidad(especialidad)
            print("✅ Especialidad agregada.")
        except Exception as e:
            print(f"⚠️ Error: {e}")

    def agendar_turno(self):
        try:
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            especialidad = input("Especialidad: ")
            fecha_str = input("Fecha y hora (aaaa-mm-dd HH:MM): ")
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
            self.__clinica.agendar_turno(dni, matricula, especialidad, fecha)
            print("✅ Turno agendado.")
        except Exception as e:
            print(f"⚠️ Error: {e}")

    def emitir_receta(self):
        try:
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            medicamentos = input("Medicamentos (separados por coma): ").split(",")
            self.__clinica.emitir_receta(dni, matricula, [m.strip() for m in medicamentos])
            print("✅ Receta emitida.")
        except Exception as e:
            print(f"⚠️ Error: {e}")

    def ver_historia_clinica(self):
        try:
            dni = input("DNI del paciente: ")
            historia = self.__clinica.obtener_historia_clinica(dni)
            print(historia)
        except Exception as e:
            print(f"⚠️ Error: {e}")

    def ver_turnos(self):
        for t in self.__clinica.obtener_turnos():
            print(t)

    def ver_pacientes(self):
        for p in self.__clinica.obtener_pacientes():
            print(p)

    def ver_medicos(self):
        for m in self.__clinica.obtener_medicos():
            print(m)
