from data import productos
from services.productos import Productos
from services.embutidos import Embutidos
from services.farmacia import Farmacia
from services.alimentos import Alimentos
from services.congelados import Congelados
from services.electronicos import Electronicos
from services.juguetes import Juguetes
from services.limpieza import Limpieza
from services.mascotas import Mascotas
from services.panaderia import Panaderia
from services.vinos_y_licores import Vinos_y_licores


def agregar(opcion):
    if opcion == 0:
        producto = Productos(input(' NOMBRE: '), 'General', int(input(' PRECIO: ')))
        producto.push(productos)

    elif opcion == 1:
        print("ALIMENTO: ")
        producto = Alimentos(input(' NOMBRE: '), 'ALimentos', int(input(' PRECIO: ')), input(' CADUCIDAD: '), input(' CANTIDAD NETA: '), input(' FECHA DE PRODUCCION: '))
        producto.push(productos)

    elif opcion == 2:
        print("ALIMENTO CONGELADO: ")
        producto = Congelados(input(' NOMBRE: '), 'Congelados', int(input(' PRECIO: ')), input(' CADUCIDAD: '), input(' CANTIDAD NETA: '), input(' FECHA DE PRODUCCION: '), input(' TEMPERATURA: '), input(' MARCA: '))
        producto.push(productos)

    elif opcion == 3:
        print("ELECTRONICOS: ")
        producto = Electronicos(input(' NOMBRE: '), 'Electronicos', int(input(' PRECIO: ')), input(' MARCA: '), input(' UTILIDAD: '), input(' PESO: '))
        producto.push(productos)

    elif opcion == 4:
        print("MASCOTAS: ")
        producto = Mascotas(input(' NOMBRE: '), 'Mascotas', int(input(' PRECIO: ')), input(' SECCION: '), input(' ESPECIE: '), input(' EDAD: '), input(' MARCA: '), input(' MANTENIMIENTO: '))
        producto.push(productos)

    elif opcion == 5:
        print("EMBUTIDOS: ")
        producto = Embutidos(input(' NOMBRE: '), 'Embutidos', int(input(' PRECIO: ')), input(' MARCA: '), input(' CLASIFICACIÓN: '))
        producto.push(productos)

    elif opcion == 6:
        print("PRODUCTOS DE LIMPIEZA: ")
        producto = Limpieza(input(' NOMBRE: '), 'Limpieza', int(input(' PRECIO: ')), input(' TAMAÑO: '), input(' MARCA: '), input(' PRESENTACIÓN'), input('SECCIÓN'), input('TIPO DE PRODUCTO'))
        producto.push(productos)

    elif opcion == 7:
        print("JUGUETES: ")
        producto = Juguetes(input(' NOMBRE: '), 'Juguetes', int(input(' PRECIO: ')), input(' MARCA: '), input(' COLOR: '),int(input(' TAMAÑO: ')),input(' MATERIAL: '),int(input(' PESO:')))
        producto.push(productos)

    elif opcion == 8:
        print("VINOS Y LICORES: ")
        producto = Vinos_y_licores(input(' NOMBRE: '), 'Vinos y licores', int(input(' PRECIO: ')), int(input(' CONTENIDO: ')), input(' SABOR: ')), int(input(' PORCENTAJE DE ALCOHOL: '))
        producto.push(productos)

    elif opcion == 9:
        print("PANADERIA: ")
        producto = Panaderia(input(' NOMBRE: '), 'Panaderia', int(input(' PRECIO: ')), input(' MARCA: '), float(input(' PESO: ')), input(' CADUCIDAD: '), input(' TIPO DE PAN: '), input(' SABOR: '))
        producto.push(productos)

    elif opcion == 10:
        print("FARMACIA: ")
        producto = Farmacia(input(' NOMBRE: '), 'Farmacia', int(input(' PRECIO: ')), int(input(' GRAMAJE: ')), int(input(' DOSIS: ')), input(' ENFERMEDAD: '), input(' TIPO: '), input(' CONTROLADO: '))
        producto.push(productos)

    elif opcion == 11:
        print("FRUTAS Y VERDURAS: ")
        producto = Farmacia(input(' NOMBRE: '), 'Frutas y verduras', int(input(' PRECIO: ')), int(input(' NETO: ')))
        producto.push(productos)
