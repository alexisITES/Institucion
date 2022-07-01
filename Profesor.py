from Persona import Persona


class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, dni, tituloUniversitario, carrera, sueldo, estadoCivil='Soltero') -> None:
        super().__init__(nombre, apellido, edad, dni, carrera, estadoCivil)
        self.tituloUniversitario = tituloUniversitario
        self.sueldo = sueldo
