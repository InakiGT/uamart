class Productos():
    def __init__(self, id, nombre, tipo, precio):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

    def __del__(self):
        pass

    def mostrar_datos(self):
        print ("PRODUCTO: " + str(self.ID) + "\nNOMBRE: " + self.nombre + "\nCATEGORIA: " + self.tipo + "\nPRECIO: $" + str(self.precio))

    def comprar(self):
        print("Inserte la cantidad de " + self.nombre + " que desea comprar")
        cant = int(input())
        compra = cant * self.precio
        print("El total de su compra es: " + str(compra))
        return compra

    def pago_tarjeta(self, compra):
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


    def pago_efectivo(self, compra):
        print("A ESCOGIDO LA OPCION DE PAGAR CON EFECTIVO")
        print(" La cantidad a pagar es: " + str(compra))
        x = int(input("Inserte el dinero: "))
        if(x==compra):
            print("Gracias por su compra")
        elif(x!=compra):
            cambio = x - compra
            print("Su cambio es $" + str(cambio) + ".00 gracias por su compra")
