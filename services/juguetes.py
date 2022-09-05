from services.productos import Productos


class Juguetes(Productos):
    def __init__(self, nombre, tipo, precio, marca, color, tamanio, material, peso):
        super().__init__(nombre, tipo, precio)
        self.marca = marca
        self.color = color
        self.tamanio = tamanio
        self.material = material
        self.peso = peso

    def __del__(self):
        pass

    @staticmethod
    def mostrar_datos(producto):
        Productos.mostrar_datos(producto)
        print ("MARCA:  "+ producto['marca'] + "\nCOLOR: "+ producto['color'] + "\nTAMAÑO: " + str(producto['tamanio']) + " cm \nMATERIAL: " + producto['material'] + "\nPESO:" +str(producto['peso']) + " gr.")


    def push(self, array):
        nuevo_producto = {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'precio': self.precio,
            'marca': self.marca,
            'color': self.color,
            'tamanio': self.tamanio,
            'material': self.material,
            'peso': self.peso,
        }
        array.append(nuevo_producto)
