from dominio.CuentaAhorro import CuentaAhorro
from dominio.Titular import Titular


class CuentaAhorroService:

    titular = Titular(None,None,None,None,None,None,None)

    titular.crearPersona()

    cuenta = CuentaAhorro(123, 0, titular.nombre)

   # Cuenta =  Titular(None,None,None,None,None,None,None)

    cuenta.crearCuenta()
    cuenta.verCuenta(titular)
    cuenta.consignarCuenta()
    cuenta.verCuenta(titular)
    cuenta.retirar_cuenta()
    cuenta.verCuenta(titular)
