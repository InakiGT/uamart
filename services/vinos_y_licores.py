from services.productos import Productos


class Vinos_y_licores(Productos):
    def __init__(self, nombre, tipo, precio, mililitros, sabor, porcentaje):
        super().__init__(nombre, tipo, precio)
        self.mililitros = mililitros
        self.sabor = sabor
        self.porcentaje = porcentaje

    def __del__(self):
        pass

    def mostrar_datos(producto):
        Productos.mostrar_datos(producto)
        print ("CONTENIDO: " + str(producto['mililitros']) + " ml" + "\n SABOR: " + producto['sabor'] + "\nPORCENTAJE DE ALCOHOL: " + str(producto['porcentaje']) + "%")

    def push(self, array):
        nuevo_producto = {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'precio': self.precio,
            'mililitros': self.mililitros,
            'sabor': self.sabor,
            'porcentaje': self.porcentaje,
        }
        array.append(nuevo_producto)
