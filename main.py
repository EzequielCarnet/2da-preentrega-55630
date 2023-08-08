from Paquete.modulo1 import *
from Paquete.modulo2 import *

computadora = Articulos("computadora", "hp", "1" )
celular = Articulos("celular", "samsung", "2")
tablet = Articulos("tablet", "Apple", "3")

cargar_clientes()

cliente4 = Cliente("china", "suarez","quelaapario 333", "27334582")



comprar(cliente4)


guardar_clientes()

for cliente in lista_clientes:
    print(f"Cliente: {cliente.nombre} {cliente.apellido}")
    print(f"Productos comprados: {cliente.productos_comprados}\n")
