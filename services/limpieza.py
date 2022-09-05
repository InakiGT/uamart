from services.productos import Productos


class Limpieza(Productos):
    def __init__(self, nombre, tipo, precio, tamanio, marca, presentacion, seccion, tipo_jabon):
        super().__init__(nombre, tipo, precio)
        self.tamanio = tamanio
        self.marca = marca
        self.presentacion = presentacion
        self.seccion = seccion
        self.tipo = tipo
        self.tipo_jabon = tipo_jabon

    def __del__(self):
        pass

    @staticmethod
    def mostrar_datos(producto):
        Productos.mostrar_datos(producto)
        print(" TAMAÑO: " + producto['tamanio'] + "\n MARCA: " + producto['marca'] + "\nPRESENTACÓN: " + producto['presentacion'] + "\nSECCIÓN: " + producto['seccion'] + " \nTIPO DE JABON: " + producto['tipo_jabon'])

    def push(self, array):
        nuevo_producto = {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'precio': self.precio,
            'marca': self.marca,
            'presentacion': self.presentacion,
            'tamanio': self.tamanio,
            'seccion': self.seccion,
            'tipo_jabon': self.tipo_jabon
        }
        array.append(nuevo_producto)
