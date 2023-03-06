from cliente import Cliente,c1
from producto import Producto,p1
from vendedor import Vendedor,v1
from datetime import date, datetime

entrada = ''
while True:
    print('----------MENU----------')
    print('1. Crear Cliente')
    print('2. Mostrar Clientes')
    print('3. Mostrar Saldo del Cliente')
    print('4. Añadir Saldo al Cliente')
    print('5. Crear Productos')
    print('6. Mostrar productos')
    print('7. Comprar productos \n 0. SALIR')
    entrada = str(input('Que desea hacer? \n'))
    if entrada == '1':
        c1.agregar_clientes()

    elif entrada == '2':
        c1.mostrar_clientes()
    elif entrada == '3':
        c1.mostrar_saldo()

    elif entrada == '4':
        c1.agregar_saldo()
    elif entrada == '5':
        p1.crear_producto()
    elif entrada == '6':
        p1.mostrar_productos()
    elif entrada == '7':
        v1.vender(p1,32)
    elif entrada == '0':
        break
    else:
        print('entrada no valida. Porfavor selecciona una opcion')
# if __name__ == '__main__':
#     pass
