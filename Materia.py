from mailbox import NoSuchMailboxError


class Materia():
    def __init__(self, nombre, horario, promedioAprobacion, esVirtual) -> None:
        self.nombre = nombre
        self.horario = horario
        self.promedioAprobacion = promedioAprobacion
        self.esVirtual = esVirtual
