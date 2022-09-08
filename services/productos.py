import uuid


class Productos():
    def __init__(self, nombre, tipo, precio):
        self.id = uuid.uuid1().__str__()
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

    def __del__(self):
        pass

    @staticmethod
    def mostrar_datos(producto):
        print ("PRODUCTO: " + str(producto['id']) + "\nNOMBRE: " + producto['nombre'] + "\nCATEGORIA: " + producto['tipo'] + "\nPRECIO: $" + str(producto['precio']))

    @staticmethod
    def get(array, id):
        for producto in array:
            if producto['id'] == id:
                return producto

    def push(self, array):
        nuevo_producto = {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'precio': self.precio,
        }
        array.append(nuevo_producto)

    @staticmethod
    def patch(array, id, nuevo_producto):
        Productos.delete(array, id)
        array.append(nuevo_producto)

    @staticmethod
    def delete(array, id):
        for i in range(len(array)):
            if array[i]['id'] == id:
                del array[i]
                print("Producto eliminado")
                break
            elif i == len(array) - 1:
                print("Producto no encontrado")

    @staticmethod
    def comprar(producto):
        print("Inserte la cantidad de " + producto['nombre'] + " que desea comprar")
        cant = int(input())
        compra = cant * int(producto['precio'])
        print("El total de su compra es: " + str(compra))
        return compra

    @staticmethod
    def pago_tarjeta(compra):
        print("A ESCOGIDO LA OPCION DE PAGAR CON TARJETA")
        print(" La cantidad a pagar es: " + str(compra))
        MSI = input("Desea pagar a meses sin intereses? SI/NO: ")
        print(MSI)
        if (MSI == 'SI'):
            print(" ESCOJA LA OPCION QUE DESEA")
            print("(0) 3  MSI ")
            print("(1) 6  MSI ")
            print("(2) 12 MSI ")
            print("(3) 24 MSI ")
            x = int(input("Inserta la opcion que deseas: "))
            if (x==0):
                print("Has escogido pagar a 3 MSI ")
                print("El primer pago es de " + str(compra/3) )
            elif (x==1):
                print("Has escogido pagar a 6 MSI ")
                print("El primer pago es de " + str(compra/6))
            elif (x==2):
                print("Has escogido pagar a 12 MSI ")
                print("El primer pago es de " + str(compra/12))
            elif (x==3):
                print("Has escogido pagar a 24 MSI ")
                print("El primer pago es de " + str(compra/24))

        elif(MSI == 'NO'):
            print("Inserte la tarjeta en el pinpad")

        else:
            print("Escoja una opcion valida")

    @staticmethod
    def pago_efectivo(compra):
        print("A ESCOGIDO LA OPCION DE PAGAR CON EFECTIVO")
        print(" La cantidad a pagar es: " + str(compra))
        x = int(input("Inserte el dinero: "))
        if x == compra:
            print("Gracias por su compra")
        elif x != compra:
            cambio = x - compra
            print("Su cambio es $" + str(cambio) + ".00 gracias por su compra")
