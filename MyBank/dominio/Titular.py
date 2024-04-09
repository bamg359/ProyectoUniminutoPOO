from dominio.Persona import Persona


class Titular(Persona):


    producto = None
    clave = None

    def __init__(self,id, nombre, apellido, correo,telefono, producto, clave):
        super().__init__(id, nombre, apellido, correo, telefono)
        self._producto = producto
        self._clave = clave


    #clientes = {}

    def crearPersona(self, producto):
        super().crearPersona()
        value = int(input("Indique codigo producto 1. Ahorro 2. Credito"))
        self._producto = producto.productos[value]
        self._clave = int(input("Clave: "))
        self.clientes[self._id] = self._nombre, self._apellido, self._correo, self._telefono,self._producto,self._clave

    def ver_persona(self):
        for i in self.clientes.items():
            print(i)
