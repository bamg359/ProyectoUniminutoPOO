



class Producto:

    def __init__(self, id_prod, nombre_prod):

        self.__id_prod = id_prod
        self.__nombre_prod = nombre_prod



    @property
    def id_prod(self):
        return self.__id_prod

    @id_prod.setter
    def id_prod(self, id_prod):
        self.__id_prod = id_prod

    @property
    def nombre_prod(self):
        return self.__nombre_prod

    @nombre_prod.setter
    def nombre_pro(self, nombre_prod):
        self.__nombre_prod = nombre_prod

    productos = {}
    producto_list = {}

    print(f"Esto es interno{productos}")

    def  crear_prod(self):

        self.__id_prod = int(input("Codigo Producto: "))
        self.__nombre_prod = input("Nombre del producto: ")

        self.productos[self.__id_prod]= self.__nombre_prod


    def verprod(self):
        for i in self.productos.items():
            print(i)









