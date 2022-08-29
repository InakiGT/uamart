from services.productos import Productos


class Alimentos(Productos):
    def __init__(self, id, nombre, tipo, precio, caducidad, neto, produccion):
        super().__init__(id, nombre, tipo, precio)
        self.caducidad = caducidad
        self.neto = neto
        self.produccion = produccion

    def __del__(self):
        pass

    def mostrar_datos(self):
        super().mostrar_datos()
        print ("CADUCIDAD: " + self.caducidad + "\nCANTIDAD NETA: " + str(self.neto) + "g\nFECHA DE PRODUCCIÓN: " + self.produccion)
