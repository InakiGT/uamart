from services.productos import Productos


class Juguetes(Productos):
    def __init__(self, id, nombre, tipo, precio, marca, color, tamanio, material, peso):
        super().__init__(id, nombre, tipo, precio)
        self.marca = marca
        self.color = color
        self.tamanio = tamanio
        self.material = material
        self.peso = peso

    def __del__(self):
        pass

    def mostrar_datos(self):
        super().mostrar_datos()
        print ("MARCA:  "+ self.marca + "\nCOLOR: "+ self.color + "\nTAMAÑO: " + str(self.tamanio) + " cm \nMATERIAL: " + self.material + "\nPESO:" +str(self.peso) + " gr.")
