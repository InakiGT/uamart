from services.productos import Productos


class Electronicos(Productos):
    def __init__(self, nombre, tipo, precio, marca, utilidad, peso):
        super().__init__(nombre, tipo, precio)
        self.marca = marca
        self.utilidad = utilidad
        self.peso = peso

    def __del__(self):
        pass

    @staticmethod
    def mostrar_datos(producto):
        Productos.mostrar_datos(producto)
        print("MARCA: " + producto['marca'] + "\nUTILIDAD: " + producto['utilidad'] + "\nPESO: " + str(producto['peso']) + "g")

    def push(self, array):
        nuevo_producto = {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'precio': self.precio,
            'marca': self.marca,
            'utilidad': self.utilidad,
            'peso': self.peso,
        }
        array.append(nuevo_producto)
