from services.productos import Productos


class Limpieza(Productos):
    def __init__(self, id, nombre, tipo, precio, tamanio, marca, presentacion, seccion, tipo_jabon):
        super().__init__(id, nombre, tipo, precio)
        self.tamanio = tamanio
        self.marca = marca
        self.presentacion = presentacion
        self.seccion = seccion
        self.tipo = tipo
        self.tipo_jabon = tipo_jabon

    def __del__(self):
        pass
    def mostrar_datos(self):
        super().mostrar_datos()
        print(" TAMAÑO: " + self.tamanio + "\n MARCA: " + self.marca + "\nPRESENTACÓN: " + self.presentacion + "\nSECCIÓN: " + self.seccion + " \nTIPO DE JABON: " + self.tipo_jabon)
