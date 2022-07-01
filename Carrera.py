class Carrera():
    key = 0

    def __init__(self,  nombre, duracion, descripcion, materias, especialidad, identidad=key,) -> None:
        self.id = identidad
        self.nombre = nombre
        self.duracion = duracion
        self.descripcion = descripcion
        self.materias = materias
        self.especialidad = especialidad
        key += 1

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}.\nDescripcion: {self.descripcion}'
