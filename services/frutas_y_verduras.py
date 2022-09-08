from services.productos import Productos

class Frutas_Y_Verduras(Productos):
    def __init__(self, nombre, tipo, precio, neto):
        super().__init__(nombre, tipo, precio)
        self.neto = neto

    def __del__(self):
        pass

    @staticmethod
    def mostrarDatos(producto):
        super().mostrarDatos()
        print ("CANTIDAD NETA: " + str(producto['neto']) + " kg.")


    def push(self, array):
        nuevo_producto = {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'precio': self.precio,
            'neto': self.neto,
        }
        array.append(nuevo_producto)
