
class CuentaAhorro:

    cuentas_de_ahorro = {}

    def __init__(self, num_cuenta, saldo,titular, id_titular):
        self._cod_banco = 15
        self._sucursal = 1
        self._ciudad = "05631"
        self._num_cuenta= f"{self._cod_banco}{self._sucursal}{self._ciudad}"
        self._saldo = saldo
        self._titular = titular
        self._id_titular = id_titular



    @property
    def num_cuenta(self):
        return self._num_cuenta

    @num_cuenta.setter
    def num_cuenta(self, num_cuenta):
        self._num_cuenta = num_cuenta

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def id_titular(self):
        return self._id_titular

    @id_titular.setter
    def id_titular(self, id_titular):
        self._id_titular = id_titular

    cuentas_de_ahorro = {}

    def crearCuenta(self,titular):

        self._id_titular = input("Ingrese la cedula del Titular")
        self._titular = titular.clientes[self._id_titular][0]
        print(self._titular)
        self._num_cuenta = self._num_cuenta + self._id_titular
        print(self._num_cuenta)
        self._saldo = int(input("Saldo"))
        self.cuentas_de_ahorro[self._num_cuenta] = [self._id_titular, self._titular, self._saldo]
        self._num_cuenta = ""
        self._id_titular=""

    def consignarCuenta(self):
        self._num_cuenta = input("Indique el numero de cuenta destino: ")
        consignacion = int(input("Valor a consignar"))
        cuenta_destino = self._num_cuenta
        print(f"cuenta destino: {cuenta_destino}")
        saldo = self.cuentas_de_ahorro[cuenta_destino][2]
        print(f"Saldo detino: {saldo}")

        if consignacion > 0:
            #for cuenta_destino in self.cuentas_de_ahorro:
            self.cuentas_de_ahorro[cuenta_destino][2] = (saldo + consignacion)
        else:
            print("Valor a consignar no puede ser menor a cero ni cero")

        saldo = self.cuentas_de_ahorro[cuenta_destino][2]
        print(f"Nuevo Saldo detino: {saldo}")





    def retirar_cuenta(self):
        self._num_cuenta = input("Indique el numero de cuenta a realizar el retiro: ")
        cuenta = self._num_cuenta
        saldo = self.cuentas_de_ahorro[cuenta][2]
        retiro = int(input("Valor a retirar: "))
        if retiro < saldo:
            self.cuentas_de_ahorro[cuenta][2] = saldo - retiro
            print(f"Valor retiro{retiro}")
            saldo = self.cuentas_de_ahorro[cuenta][2]
            print(f"Su nuevo saldo es{saldo}")
        else:
            print("Saldo Insuficiente")

    def verCuenta(self):
        #print(f"Titular{self._titular}")
        #print(f"Numero de Cuenta{self._num_cuenta}")
        #print(f"saldo: {self._saldo}")
        for item in self.cuentas_de_ahorro.items():
            print(item)


    def tranferirACuenta(self):
        self._num_cuenta = input("Indique el numero de cuenta destino: ")
        cuenta_destino = self._num_cuenta
        print(f"cuenta destino: {cuenta_destino}")
        saldo_destino = self.cuentas_de_ahorro[cuenta_destino][2]
        print(f"Saldo detino: {saldo_destino}")

        self._num_cuenta = input("INdique la cuenta origen: ")
        cuenta_origen = self._num_cuenta
        print(f"cuenta Origen: {cuenta_origen}")
        saldo_origen = self.cuentas_de_ahorro[cuenta_origen][2]
        print(f"saldo Origen: {saldo_origen}")
        monto = int(input("Indique el valor a transferir: "))
        saldo_validador = saldo_origen - monto

        if saldo_validador >= 0:
            #for cuenta_origen in self.cuentas_de_ahorro:
            self.cuentas_de_ahorro[cuenta_origen][2]= saldo_origen - monto
            #for cuenta_destino in self.cuentas_de_ahorro:
            self.cuentas_de_ahorro[cuenta_destino][2] = (saldo_destino + monto)
        else:
            print("Saldo insuficiente")
        saldo_or = self.cuentas_de_ahorro[cuenta_origen][2]
        print(f"Nuevo saldo Origen: {saldo_or}")
        saldo = self.cuentas_de_ahorro[cuenta_destino][2]
        print(f"Nuevo Saldo detino: {saldo}")


