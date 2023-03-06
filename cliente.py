from dataclasses import dataclass, asdict
from datetime import date, datetime

@dataclass
class Cliente:
    id_cliente:int
    nombre:str
    apellido:str
    correo:str
    fecha_registro:str
    _saldo:int
    attr_op =str
    lista_clientes = []

    #agregamos clientes al programa
    def agregar_clientes(self):

        client_id = len(self.lista_clientes) + 1
        nombre = str(input('Ingresa el nombre del cliente: '))
        apellido = str(input('Ingresa el apellido del cliente: '))
        correo = str(input('Ingresa el correo del cliente: '))
        fecha_registro = datetime.now().date().strftime('%Y-%m-%d')
        saldo = int(input('Ingresa el saldo del cliente: '))
        new_cliente = Cliente(client_id,nombre,apellido,correo,fecha_registro,saldo)
        print(f'El cliente {nombre.upper()} ha sido agregado correctamente. ')
        self.lista_clientes.append(asdict(new_cliente))
    
    #Mostramos los clientes del programa
    def mostrar_clientes(self):
        if self.lista_clientes == []:
            print('No existen clientes registrados actualmente. ')
            op = input('Deseas agregar clientes. (S/N) \n ').upper()
            while not op in ['S','N']:
                print('Comando no reconocido. ')
                op = input('Porfavor ingresa uno de estos: (S/N) \n').upper()
            if op.upper() == 'S':
                c1.agregar_clientes()
                
            else:
                pass
        else:
            print('----------LISTA CLIENTES----------')
            for cliente in self.lista_clientes:
                print('ID: ' + str(cliente['id_cliente']) + '---> CLIENTE: ' + str.upper((cliente['nombre'])) + '\n')
                
                
    def mostrar_saldo(self):
        if len(self.lista_clientes) >= 1:
            for cliente in self.lista_clientes:
                print('ID: ' + str(cliente['id_cliente']) + '---> CLIENTE: ' + str.upper((cliente['nombre'])))
    
            entrada = int(input('Ingresa el ID del cliente que quieres mostrar su saldo: '))
            exist_client = False
            while not exist_client:
                if cliente['id_cliente'] == entrada:
                    exist_client = True
                    print(f'El saldo del cliente ' + str.upper((cliente['nombre'])) + ' es de ' + str(cliente['_saldo']))
                else:
                    print('El cliente no se encuentra o no existe. \n')
                    for cliente in self.lista_clientes:
                        print('ID: ' + str(cliente['id_cliente']) + '---> CLIENTE: ' + str.upper((cliente['nombre'])))
                    entrada = int(input('Porfavor ingresa su ID nuevamente: \n'))

        elif len(self.lista_clientes) == 0:
            print('No existen clientes registrados. ')
            op = input('Deseas agregar clientes. (S/N) \n ').upper()
            while not op in ['S','N']:
                print('Comando no reconocido. ')
                op = input('Porfavor ingresa uno de estos: (S/N) \n').upper()
            if op.upper() == 'S':
                c1.agregar_clientes()
                
            else:
                pass
    def agregar_saldo(self):
        if len(self.lista_clientes) == 0:
            print('No existen clientes actualmente en la DB. ')
        else:
            for cliente in self.lista_clientes:
                print('ID:' + str(cliente['id_cliente']) + '---> CLIENTE: ' + str.upper((cliente['nombre'])))
            
            id_cliente = int(input('Ingresa el ID del cliente que quieres agregar saldo: '))
            cliente_encontrado =False
        
            for cliente in self.lista_clientes:
                if cliente['id_cliente'] == id_cliente:
                    print(f'El saldo actual del cliente es: ' + str(cliente['_saldo']))
                    add_saldo = int(input('Cuanto saldo desea añadir? '))
                    cliente['_saldo'] += add_saldo
                    cliente_encontrado = True
                    print(f'Se ha añadido {add_saldo} al saldo del cliente. El saldo actual es ' + str(cliente['_saldo']))
                else:
                    cliente_encontrado = False
                    print('El cliente no ha sido encontrado o no existe. ')
                        
c1 = Cliente(0,'Juan','Lopez','jlopez@gmail.com','12-02-2022',3000)


