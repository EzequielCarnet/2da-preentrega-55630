#clases

class Cliente:
    def __init__(self, nombre, apellido, domicilio, DNI):
        self.nombre = nombre
        self.apellido = apellido
        self.domicilio = domicilio
        self.DNI = DNI
        self.productos_comprados=[]
       
    def __str__(self):
        return f"Se creó el cliente {self.apellido}, {self.nombre}"



class Articulos:
    def __init__(self, articulo, marca, codigo):
        self.articulo = articulo
        self.marca = marca 
        self.codigo = codigo
    def __str__(self):
        return f"Se creó el articulo {self.articulo}, {self.marca}"





