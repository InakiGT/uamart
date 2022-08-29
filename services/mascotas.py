from services.productos import Productos


class Mascotas(Productos):
    def __init__(self, id, nombre, tipo, precio, categoria, especie, edad, marca, mantenimiento):
        super().__init__(id, nombre, tipo, precio)
        self.categoria = categoria
        self.especie = especie
        self.edad = edad
        self.marca = marca
        self.mantenimiento = mantenimiento

    def __del__(self):
        pass
    def mostrar_datos(self):
        super().mostrar_datos()
        print("SECCION: " + self.categoria + "\nESPECIE:" + self.especie + "\nEDAD: " + self.edad + "\nMARCA: " + self.marca + "\nCUIDADOS ESPECIALES: " + self.mantenimiento)
