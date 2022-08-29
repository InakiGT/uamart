from services.embutidos import Embutidos
from services.productos import Productos
from services.alimentos import Alimentos
from services.congelados import Congelados
from services.electronicos import Electronicos
from services.juguetes import Juguetes
from services.limpieza import Limpieza
from services.mascotas import Mascotas
from services.panaderia import Panaderia
from services.vinos_y_licores import Vinos_y_licores


def agregar():
    ID = x - 1
    if(b==0):
        productos.append(Productos(ID, input(' NOMBRE: '), 'General', int(input(' PRECIO: '))))
    elif(b==1):
        print("ALIMENTO: ")
        productos.append(Alimentos(ID, input(' NOMBRE: '), 'ALimento', int(input(' PRECIO: ')), input(' CADUCIDAD: '), input(' CANTIDAD NETA: '), input(' FECHA DE PRODUCCION: ')))
    elif(b==2):
        print("ALIMENTO CONGELADO: ")
        productos.append(Congelados(ID, input(' NOMBRE: '), 'Congelados', int(input(' PRECIO: ')), input(' CADUCIDAD: '), input(' CANTIDAD NETA: '), input(' FECHA DE PRODUCCION: '), input(' TEMPERATURA: '), input(' MARCA: ')))
    elif(b==3):
        print("ELECTRONICOS: ")
        productos.append(Electronicos(ID, input(' NOMBRE: '), 'Electronicos', int(input(' PRECIO: ')), input(' MARCA: '), input(' UTILIDAD: '), input(' PESO: ')))
    elif(b==4):
        print("MASCOTAS: ")
        productos.append(Mascotas(ID, input(' NOMBRE: '), 'Mascotas', int(input(' PRECIO: ')), input(' SECCION: '), input(' ESPECIE: '), input(' EDAD: '), input(' MARCA: '), input(' MANTENIMIENTO: ')))
    elif(b==5):
        print("EMBUTIDOS: ")
        productos.append(Embutidos(ID, input(' NOMBRE: '), 'Embutidos', int(input(' PRECIO: ')), input(' MARCA: '), input(' CLASIFICACIÓN: ')))
    elif(b==6):
        print("PRODUCTOS DE LIMPIEZA: ")
        productos.append(Limpieza(ID, input(' NOMBRE: '), 'PRODUCTOS DE LIMPIEZA', int(input(' PRECIO: ')), input(' TAMAÑO: '), input(' MARCA: '), input(' PRESENTACIÓN'), input('SECCIÓN'), input('TIPO DE PRODUCTO')))
    elif(b==7):
        print("JUGUETES: ")
        productos.append(Juguetes(ID, input(' NOMBRE: '), 'Juguetes', int(input(' PRECIO: ')), input(' MARCA: '), input(' COLOR: '),int(input(' TAMAÑO: ')),input(' MATERIAL: '),int(input(' PESO:'))))
    elif(b==8):
        print("VINOS Y LICORES: ")
        productos.append(Vinos_y_licores(ID, input(' NOMBRE: '), 'Vinos y licores', int(input(' PRECIO: ')), int(input(' CONTENIDO: ')), input(' SABOR: ')), int(input(' PORCENTAJE DE ALCOHOL: ')))
    elif(b==9):
        print("PANADERIA: ")
        productos.append(Panaderia(ID, input(' NOMBRE: '), 'Panaderia', int(input(' PRECIO: ')), input(' MARCA: '), float(input(' PESO: ')), input(' CADUCIDAD: '), input(' TIPO DE PAN: '), input(' SABOR: ')))

productos = []

productos.append(Congelados(0, 'Helado', 'Congelados', 60, '30/Ago/2022', 1000, '15/Ago/2022', 12, 'Holanda'))
productos.append(Alimentos(2, 'Pan', 'Congelados', 70, '14/Agosto/2022', 12, '8/Agosto/2022'))
productos.append(Limpieza(3, 'Limpiador Multiusos', 'Producto de Limpieza', 23, 'Botella 500 ml', 'FABULOSO', 'Liquido ','Limpiadores', 'Superficies'))
productos.append(Juguetes(4,'Muñeca', 'Juguetes', 350, 'Barbie', 'Rosa', 25, 'Plastico', '450'))
productos.append(Mascotas(5, 'Croquetas', 'Mascotas', '650', 'Alimentos', 'Perros', 'Adultos', 'Purina', 'Conservese en un lugar fresco y seco'))
productos.append(Vinos_y_licores(6, 'Bacardi','Vinos y licores', 275, 750,'Frambruesa',35))
productos.append(Panaderia(7,'Dona', 'Panaderia', 7, 'Casero', 0.025, '31/Agosto/2022', 'Dulce', 'Chocolate'))

x = 8

while True:
    print("/// MENU /// ")
    print(" (0) Mostrar productos ")
    print(" (1) Agregar un producto ")
    print(" (2) Comprar producto ")
    print(" (3) Eliminar producto ")
    a = int(input("Inserte la opcion que desee: "))
    print(a)

    if(a==0):
        for i in range (x):
            productos[i].mostrar_datos()
            print ("----------")

    elif (a==1):
        x = x + 1
        print("              /// AGREGAR UN PRODUCTO /// ")
        print(" --- Escoja el tipo de producto que desea agregar --- ")
        print("                     (0) Producto ")
        print("                     (1) Alimento ")
        print("                     (2) Congelado ")
        print("                     (3) Electronico ")
        print("                     (4) Mascotas ")
        print("                     (5) Embutidos ")
        print("                     (6) Productos de Limpieza ")
        print("                     (7) Juguetes ")
        print("                     (8) Vinos y Licores ")
        print("                     (9) Panaderia ")
        b = int(input("            Inserta una opcion: "))
        agregar()

    elif (a==2):
        print(" /// COMPRAR ///")
        ID = int(input("Inserte el ID del producto que desea comprar: "))
        if (ID < x):
            compra = productos[ID].comprar()
            print(" Desea pagar con: \n(0)Efectivo\n(1)Tarjeta")
            b = int(input())
            if(b==1):
                productos[ID].Pago_tarjeta(compra)
            if(b==0):
                productos[ID].Pago_efectivo(compra)
        else:
            print("El ID para este producto no existe")

    elif (a==3):
        print(" /// ELIMINAR ///")
        x = x - 1
        ID = int(input("Inserta el ID del procucto que deseas eliminar: "))
        productos.pop(ID)

    if(a==10):
        break
