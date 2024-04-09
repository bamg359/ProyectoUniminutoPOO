


class Persona:


    id = None
    nombre = None
    apellido = None
    correo = None
    telefono = None

    clientes = {}


    def __init__(self, id, nombre, apellido, correo, telefono):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    def crearPersona(self):
        self._id = input("Id: ")
        self._nombre = input("Nombre: ")
        self._apellido= input("Apellido: ")
        self._correo = input("Correo: ")
        self._telefono = input("Telefono: ")
