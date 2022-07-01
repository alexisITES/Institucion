from Persona import Persona


class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, dni, carrera, escuela, nota, estadoCivil='Soltero') -> None:
        super().__init__(nombre, apellido, edad, dni, carrera, estadoCivil)
        self.escuela = escuela
        self.nota = nota
