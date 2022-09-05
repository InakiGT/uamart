from data import productos
from agregar_producto import agregar
from services.alimentos import Alimentos
from services.congelados import Congelados
from services.electronicos import Electronicos
from services.embutidos import Embutidos
from services.farmacia import Farmacia
from services.juguetes import Juguetes
from services.limpieza import Limpieza
from services.mascotas import Mascotas
from services.panaderia import Panaderia
from services.productos import Productos
from services.vinos_y_licores import Vinos_y_licores

def menu():
    while True:
        print("""
            /// MENU ///
        (0) Mostrar productos
        (1) Agregar producto
        (2) Comprar producto
        (3) Eliminar producto
        (4) Buscar producto
        """)
        a = int(input("Inserte la opcion que desee: "))
        print(a)

        if a == 0:
            for producto in productos:
                print(producto)
                print ("----------")

        elif a == 1:
            print("""
                        /// AGREGAR UN PRODUCTO ///
            --- Escoja el tipo de producto que desea agregar ---
            (0) Producto
            (1) Alimento
            (2) Congelado
            (3) Electronico
            (4) Mascotas
            (5) Embutidos
            (6) Limpieza
            (7) Juguetes
            (8) Vinos y Licores
            (9) Panaderia
            (10) Farmacia
            """)
            opcion = int(input("Inserta una opcion: "))
            agregar(opcion)

        elif a == 2:
            print(" /// COMPRAR ///")
            id = input("Inserte el ID del producto que desea comprar: ")
            if next ((item for item in productos if item["id"] == id))['id'] != "":
                producto = next ((item for item in productos if item["id"] == id))
                compra = Productos.comprar(producto)
                print("""
                Desea pagar con:
                (0)Efectivo
                (1)Tarjeta
                """)
                b = int(input())
                if (b == 0):
                    Productos.pago_efectivo(compra)
                if (b == 1):
                    Productos.pago_tarjeta(compra)
            else:
                print("El ID para este producto no existe")

        elif a == 3:
            print(" /// ELIMINAR ///")
            id = input("Inserta el id del procucto que deseas eliminar: ")
            Productos.delete(productos, id)

        elif a == 4:
            print(" /// BUSCAR ///")
            id = input("Inserta el id del procucto que deseas buscar: ")
            producto = next ((item for item in productos if item["id"] == id))
            if producto['tipo'] == 'General':
                Productos.mostrar_datos(producto)
            elif producto['tipo'] == 'ALimentos':
                Alimentos.mostrar_datos(producto)
            elif producto['tipo'] == 'Congelados':
                Congelados.mostrar_datos(producto)
            elif producto['tipo'] == 'Electronicos':
                Electronicos.mostrar_datos(producto)
            elif producto['tipo'] == 'Mascotas':
                Mascotas.mostrar_datos(producto)
            elif producto['tipo'] == 'Embutidos':
                Embutidos.mostrar_datos(producto)
            elif producto['tipo'] == 'Limpieza':
                Limpieza.mostrar_datos(producto)
            elif producto['tipo'] == 'Juguetes':
                Juguetes.mostrar_datos(producto)
            elif producto['tipo'] == 'Vinos y licores':
                Vinos_y_licores.mostrar_datos(producto)
            elif producto['tipo'] == 'Panaderia':
                Panaderia.mostrar_datos(producto)
            elif producto['tipo'] == 'Farmacia':
                Farmacia.mostrar_datos(producto)
