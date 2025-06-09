class Especialidad:
    def __init__(self, tipo: str, dias: list[str]):
        if not tipo or not dias or not all(isinstance(d, str) for d in dias):
            raise ValueError("Tipo de especialidad y días válidos son obligatorios.")
        self.__tipo = tipo
        self.__dias = [d.lower() for d in dias]

    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        return dia.lower() in self.__dias

    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"
