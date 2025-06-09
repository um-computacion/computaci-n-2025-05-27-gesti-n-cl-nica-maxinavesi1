from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad

    def obtener_medico(self) -> Medico:
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora

    def __str__(self) -> str:
        return (
            f"Turno(\n"
            f"  {self.__paciente},\n"
            f"  {self.__medico},\n"
            f"  {self.__fecha_hora.strftime('%Y-%m-%d %H:%M')},\n"
            f"  {self.__especialidad}\n"
            f")"
        )
