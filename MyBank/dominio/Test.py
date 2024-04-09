from dominio.CuentaAhorro import CuentaAhorro
from dominio.Producto import Producto
from dominio.Titular import Titular

product = Producto(None,None)
titular = Titular(None, None,None,None,None,None,None)
cuenta = CuentaAhorro(None,None,None,None)



product.crear_prod()
#product.crear_prod()
product.verprod()
titular.crearPersona(product)
titular.ver_persona()
titular.crearPersona(product)
titular.ver_persona()
cuenta.crearCuenta(titular)
cuenta.verCuenta()
#cuenta.crearCuenta(titular)
#cuenta.verCuenta()
#cuenta.tranferirACuenta()
#cuenta.verCuenta()
cuenta.consignarCuenta()
cuenta.verCuenta()
cuenta.retirar_cuenta()
cuenta.verCuenta()
print(product.productos)