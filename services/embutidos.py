from services.productos import Productos


class Embutidos(Productos):
    def __init__(self, nombre, tipo, precio, marca, clasificacion, tipo_embuido):
        super().__init__(nombre, tipo, precio)
        self.marca = marca
        self.clasificacion = clasificacion
        self.tipo_embutido = tipo_embuido

    def __del__(self):
        pass

    @staticmethod
    def mostrar_datos(producto):
        Productos.mostrar_datos(producto)
        print ("MARCA: " + producto['marca'] + "\nCLASIFICACIÓN: " + producto['clasificacion'])

    def push(self, array):
        nuevo_producto = {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'precio': self.precio,
            'marca': self.marca,
            'clasificacion': self.clasificacion,
            'tipo_embutido': self.tipo_embutido,
        }
        array.append(nuevo_producto)
