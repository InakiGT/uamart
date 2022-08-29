from services.alimentos import Alimentos


class Congelados(Alimentos):
    def __init__(self, id, nombre, tipo, precio, caducidad, neto, produccion, temperatura, marca):
        super().__init__(id, nombre, tipo, precio, caducidad, neto, produccion)
        self.temperatura = temperatura
        self.marca = marca

    def __del__(self):
        pass

    def mostrar_datos(self):
        super().mostrar_datos()
        print ("TEMPERATURA: " + str(self.temperatura) + "\nMARCA: " + self.marca)
