from modelo.paciente import Paciente
from modelo.turno import Turno
from modelo.receta import Receta

class HistoriaClinica:
    def __init__(self, paciente: Paciente):
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []

    def agregar_turno(self, turno: Turno):
        self.__turnos.append(turno)

    def agregar_receta(self, receta: Receta):
        self.__recetas.append(receta)

    def obtener_turnos(self) -> list[Turno]:
        return list(self.__turnos)

    def obtener_recetas(self) -> list[Receta]:
        return list(self.__recetas)

    def __str__(self) -> str:
        turnos_str = "\n  ".join(str(t) for t in self.__turnos)
        recetas_str = "\n  ".join(str(r) for r in self.__recetas)
        return (
            f"HistoriaClinica(\n"
            f"  {self.__paciente},\n"
            f"  Turnos:\n  {turnos_str}\n"
            f"  Recetas:\n  {recetas_str}\n"
            f")"
        )
