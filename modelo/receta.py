from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        if not medicamentos or not all(isinstance(med, str) and med.strip() for med in medicamentos):
            raise ValueError("La receta debe contener al menos un medicamento válido.")
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self) -> str:
        meds = ", ".join(self.__medicamentos)
        fecha_str = self.__fecha.strftime('%Y-%m-%d %H:%M')
        return (
            f"Receta(\n"
            f"  {self.__paciente},\n"
            f"  {self.__medico},\n"
            f"  [{meds}],\n"
            f"  {fecha_str}\n"
            f")"
        )
