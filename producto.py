from dataclasses import dataclass, asdict, field

@dataclass
class Producto:
    sku:int 
    nombre:str
    categoria:str
    proveedor:str
    stock:int
    valor_neto:int
    lista_productos = []
    _impuesto : float
    # attr_op = str
    
    def crear_producto(self):
        print('--------PRODUCTO--------')
        sku =  len(self.lista_productos) + 0
        nombre = str(input('Nombre del producto: '))
        categoria = str(input('Nombre de la categoria: '))
        proveedor = str(input('Selecciona el proveedor'))
        stock = int(input('Ingresa el stock dedl producto: '))
        valor_neto = int(input('Ingresa el valor neto del producto: '))
        impuesto = 1.19
        new_producto = Producto(sku,nombre,categoria,proveedor,stock,valor_neto,impuesto)
        print(f'Producto {nombre.upper()} fue creado exitosamente. ')
        self.lista_productos.append(asdict(new_producto))

    def mostrar_productos(self):
        if len(self.lista_productos) == 0:
            print('No existen productos registrados. ')
            op = str(input('Deseas agregar productos? (S/N) ')).upper()
            while not op in ('S','N'):
                print('Comando no reconocido. Porfavor ingresa las opciones dadas: (S/N) ')
                op = str(input('Deseas agregar productos?')).upper()
            if op == 'S':
                p1.crear_producto()
            else:
                pass
        else:
            for producto in self.lista_productos:
                print(producto)
                return producto
                
p1 = Producto(0,'','','',0,0,0)
