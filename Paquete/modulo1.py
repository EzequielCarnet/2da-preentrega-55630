#clases

import json

archivo_clientes = "clientes.json"
lista_clientes = []

class Cliente:
    def __init__(self, nombre, apellido, domicilio, DNI):
        self.nombre = nombre
        self.apellido = apellido
        self.domicilio = domicilio
        self.DNI = DNI
        self.productos_comprados = []
        self.fecha_compra = []

    def __str__(self):
        return f"Se creó el cliente {self.apellido}, {self.nombre}"
    
    def guardar_en_lista(self):
        lista_clientes.append(self)
    
    def __new__(cls, *args, **kwargs):
        instance = super(Cliente, cls).__new__(cls)
        instance.guardar_en_lista()
        return instance

def guardar_clientes():
    clientes_serializados = []
    for cliente in lista_clientes:
        cliente_serializado = {
            "nombre": cliente.nombre,
            "apellido": cliente.apellido,
            "domicilio": cliente.domicilio,
            "DNI": cliente.DNI,
            "productos_comprados": cliente.productos_comprados,
            "fecha_compra": cliente.fecha_compra
        }
        clientes_serializados.append(cliente_serializado)

    with open(archivo_clientes, "w") as archivo:
        json.dump(clientes_serializados, archivo)

def cargar_clientes():
    try:
        with open(archivo_clientes, "r") as archivo:
            clientes_serializados = json.load(archivo)
            lista_clientes.clear()
            for cliente_serializado in clientes_serializados:
                cliente = Cliente(
                    nombre=cliente_serializado["nombre"],
                    apellido=cliente_serializado["apellido"],
                    domicilio=cliente_serializado["domicilio"],
                    DNI=cliente_serializado["DNI"]
                )
                cliente.productos_comprados = cliente_serializado["productos_comprados"]
                lista_clientes.append(cliente)
    except FileNotFoundError:
        pass



class Articulos:
    def __init__(self, articulo, marca, codigo):
        self.articulo = articulo
        self.marca = marca 
        self.codigo = codigo
    def __str__(self):
        return f"Se creó el articulo {self.articulo}, {self.marca}"





