from services.productos import Productos


class Alimentos(Productos):
    def __init__(self, nombre, tipo, precio, caducidad, neto, produccion):
        super().__init__(nombre, tipo, precio)
        self.caducidad = caducidad
        self.neto = neto
        self.produccion = produccion

    def __del__(self):
        pass

    @staticmethod
    def mostrar_datos(producto):
        Productos.mostrar_datos(producto)
        print ("CADUCIDAD: " + producto['caducidad'] + "\nCANTIDAD NETA: " + str(producto['neto']) + "g\nFECHA DE PRODUCCIÓN: " + producto['produccion'])

    def push(self, array):
        nuevo_producto = {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'precio': self.precio,
            'caducidad': self.caducidad,
            'neto': self.neto,
            'produccion': self.produccion,
        }
        array.append(nuevo_producto)
