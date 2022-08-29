from services.productos import Productos


class Panaderia(Productos):
    def __init__(self, id, nombre, tipo, precio, marca, peso, caducidad, tipoDePan, sabor):
        super().__init__(id, nombre, tipo, precio)
        self.marca = marca
        self.peso = peso
        self.caducidad = caducidad
        self.tipoDePan = tipoDePan
        self.sabor = sabor

    def __del__(self):
        pass

    def mostrar_datos(self):
        super().mostrar_datos()
        print ("MARCA: " + self.marca + "\nPESO: " + str(self.peso) + "\nCADUCIDAD: " + self.caducidad + "\nTIPO DE PAN: " + self.tipoDePan + "\nSABOR: " + self.sabor)
