from services.productos import Productos


class Mascotas(Productos):
    def __init__(self, nombre, tipo, precio, categoria, especie, edad, raza, mantenimiento):
        super().__init__(nombre, tipo, precio)
        self.categoria = categoria
        self.especie = especie
        self.edad = edad
        self.raza = raza
        self.mantenimiento = mantenimiento

    def __del__(self):
        pass

    @staticmethod
    def mostrar_datos(producto):
        Productos.mostrar_datos(producto)
        print("SECCION: " + producto['categoria'] + "\nESPECIE:" + producto['especie'] + "\nEDAD: " + producto['edad'] + "\nMARCA: " + producto['marca'] + "\nCUIDADOS ESPECIALES: " + producto['mantenimiento'])

    def push(self, array):
        nuevo_producto = {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'precio': self.precio,
            'categoria': self.categoria,
            'especie': self.especie,
            'edad': self.edad,
            'raza': self.raza,
            'mantenimiento': self.mantenimiento,
        }
        array.append(nuevo_producto)
