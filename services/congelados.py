from services.alimentos import Alimentos


class Congelados(Alimentos):
    def __init__(self, nombre, tipo, precio, caducidad, neto, produccion, temperatura, marca):
        super().__init__(nombre, tipo, precio, caducidad, neto, produccion)
        self.temperatura = temperatura
        self.marca = marca

    def __del__(self):
        pass

    @staticmethod
    def mostrar_datos(producto):
        Alimentos.mostrar_datos(producto)
        print ("TEMPERATURA: " + str(producto['temperatura']) + "\nMARCA: " + producto['marca'])

    def push(self, array):
        nuevo_producto = {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'precio': self.precio,
            'caducidad': self.caducidad,
            'neto': self.neto,
            'produccion': self.produccion,
            'temperatura': self.temperatura,
            'marca': self.marca,
        }
        array.append(nuevo_producto)
