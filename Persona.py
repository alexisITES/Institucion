class Persona():
    def __init__(self, nombre, apellido, edad, dni, carrera, estadoCivil='Soltero') -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.estadoCivil = estadoCivil
        self.carrera = carrera

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}.\nApellido: {self.apellido}.\nCarrera: {self.carrera}'
