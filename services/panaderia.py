from services.productos import Productos


class Panaderia(Productos):
    def __init__(self, nombre, tipo, precio, marca, peso, caducidad, tipo_de_pan, sabor):
        super().__init__(nombre, tipo, precio)
        self.marca = marca
        self.peso = peso
        self.caducidad = caducidad
        self.tipo_de_pan = tipo_de_pan
        self.sabor = sabor

    def __del__(self):
        pass

    @staticmethod
    def mostrar_datos(producto):
        Productos.mostrar_datos(producto)
        print ("MARCA: " + producto['marca'] + "\nPESO: " + str(producto['peso']) + "\nCADUCIDAD: " + producto['caducidad'] + "\nTIPO DE PAN: " + producto['tipo_pan'] + "\nSABOR: " + producto['sabor'])

    def push(self, array):
        nuevo_producto = {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'precio': self.precio,
            'marca': self.marca,
            'peso': self.peso,
            'caducidad': self.caducidad,
            'tipo_pan': self.tipo_de_pan,
            'sabor': self.sabor,
        }
        array.append(nuevo_producto)
