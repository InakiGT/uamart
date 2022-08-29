from services.productos import Productos


class Vinos_y_licores(Productos):
    def __init__(self, id, nombre, tipo, precio, mililitros, sabor, porcentaje):
        super().__init__(id, nombre, tipo, precio)
        self.mililitros = mililitros
        self.sabor = sabor
        self.porcentaje = porcentaje

    def __del__(self):
        pass

    def mostrar_datos(self):
        super().mostrar_datos()
        print ("CONTENIDO: " + str(self.mililitros) + " ml" + "\n SABOR: " + self.sabor + "\nPORCENTAJE DE ALCOHOL: " + str(self.porcentaje) + "%")
