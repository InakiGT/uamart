from services.productos import Productos


class Embutidos(Productos):
    def __init__(self, id, nombre, tipo, precio, marca, clasificacion):
        super().__init__(id, nombre, tipo, precio)
        self.marca = marca
        self.clasificacion = clasificacion

    def __del__(self):
        pass

    def mostrar_datos(self):
        super().mostrar_datos()
        print ("MARCA: " + self.marca + "\nCLASIFICACIÓN: " + self.clasificacion)
