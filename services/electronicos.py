from services.productos import Productos


class Electronicos(Productos):
    def __init__(self, id, nombre, tipo, precio, marca, utilidad, peso):
        super().__init__(id, nombre, tipo, precio)
        self.marca = marca
        self.utilidad = utilidad
        self.peso = peso

    def __del__(self):
        pass

    def mostrar_datos(self):
        super().mostrar_datos()
        print("MARCA: " + self.marca + "\nUTILIDAD: " + self.utilidad + "\nPESO: " + str(self.peso) + "g")
