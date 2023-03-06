from dataclasses import dataclass
from producto import Producto,p1
from cliente import Cliente,c1

@dataclass
class Vendedor:
    run:str
    nombre:str
    apellido:str
    seccion:str
    _comision:float=0
    attr_op = str

    def vender(self, producto, cantidad):
        for product in producto.lista_productos:
            print(str(product['sku']) + '---->' + str(product['nombre']))
        if len(producto.lista_productos) == 0:
            print('No es posible comprar. No existen productos. ')
        else:
            try:
                entrada = int(input('Selecciona el producto que quieres comprar: '))
                while entrada >= len(producto.lista_productos):
                    print('Opción no disponible por el momento.')
                    entrada = int(input('Porfavor selecciona el producto que quieres comprar.'))
                
                cantidad = int(input('Selecciona la cantidad a comprar: '))
                prod_selec = producto.lista_productos[entrada]
                while prod_selec['stock'] < cantidad:
                    print('Stock agotado. El stock actual es ' + str(prod_selec['stock']))
                    cantidad = int(input('Ingresa la cantidad que deseas comprar: '))
                    
                prod_selec['stock'] -= cantidad
                print(f'Se compraron {cantidad} unidad(es) de ' + str(prod_selec['nombre']) + '. Stock actual: '+ str(prod_selec['stock']))
            except ValueError:
                print('Debe ingresar un número dentro de las opciones indicadas.')
v1 = Vendedor('19','felipe','mayer','ventas')
