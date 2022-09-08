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


def actualizar(opcion):

    nuevo_producto = {}

    if opcion == 'General':
        producto = Productos(input(' NOMBRE: '), 'General', int(input(' PRECIO: ')))
        nuevo_producto = {
            'id': producto.id,
            'nombre': producto.nombre,
            'tipo': producto.tipo,
            'precio': producto.precio,
        }

    elif opcion == 'ALimentos':
        print("ALIMENTO: ")
        producto = Alimentos(input(' NOMBRE: '), 'ALimentos', int(input(' PRECIO: ')), input(' CADUCIDAD: '), input(' CANTIDAD NETA: '), input(' FECHA DE PRODUCCION: '))
        nuevo_producto = {
            'id': producto.id,
            'nombre': producto.nombre,
            'tipo': producto.tipo,
            'precio': producto.precio,
            'caducidad': producto.caducidad,
            'neto': producto.neto,
            'produccion': producto.produccion,
        }

    elif opcion == 'Congelados':
        print("ALIMENTO CONGELADO: ")
        producto = Congelados(input(' NOMBRE: '), 'Congelados', int(input(' PRECIO: ')), input(' CADUCIDAD: '), input(' CANTIDAD NETA: '), input(' FECHA DE PRODUCCION: '), input(' TEMPERATURA: '), input(' MARCA: '))
        nuevo_producto = {
            'id': producto.id,
            'nombre': producto.nombre,
            'tipo': producto.tipo,
            'precio': producto.precio,
            'caducidad': producto.caducidad,
            'neto': producto.neto,
            'produccion': producto.produccion,
            'temperatura': producto.temperatura,
            'marca': producto.marca,
        }

    elif opcion == 'Electronicos':
        print("ELECTRONICOS: ")
        producto = Electronicos(input(' NOMBRE: '), 'Electronicos', int(input(' PRECIO: ')), input(' MARCA: '), input(' UTILIDAD: '), input(' PESO: '))
        nuevo_producto = {
            'id': producto.id,
            'nombre': producto.nombre,
            'tipo': producto.tipo,
            'precio': producto.precio,
            'marca': producto.marca,
            'utilidad': producto.utilidad,
            'peso': producto.peso,
        }

    elif opcion == 'Mascotas':
        print("MASCOTAS: ")
        producto = Mascotas(input(' NOMBRE: '), 'Mascotas', int(input(' PRECIO: ')), input(' SECCION: '), input(' ESPECIE: '), input(' EDAD: '), input(' MARCA: '), input(' MANTENIMIENTO: '))
        nuevo_producto = {
            'id': producto.id,
            'nombre': producto.nombre,
            'tipo': producto.tipo,
            'precio': producto.precio,
            'categoria': producto.categoria,
            'especie': producto.especie,
            'edad': producto.edad,
            'raza': producto.raza,
            'mantenimiento': producto.mantenimiento,
        }

    elif opcion == 'Embutidos':
        print("EMBUTIDOS: ")
        producto = Embutidos(input(' NOMBRE: '), 'Embutidos', int(input(' PRECIO: ')), input(' MARCA: '), input(' CLASIFICACIÓN: '))
        nuevo_producto = {
            'id': producto.id,
            'nombre': producto.nombre,
            'tipo': producto.tipo,
            'precio': producto.precio,
            'marca': producto.marca,
            'clasificacion': producto.clasificacion,
            'tipo_embutido': producto.tipo_embutido,
        }

    elif opcion == 'Limpieza':
        print("PRODUCTOS DE LIMPIEZA: ")
        producto = Limpieza(input(' NOMBRE: '), 'Limpieza', int(input(' PRECIO: ')), input(' TAMAÑO: '), input(' MARCA: '), input(' PRESENTACIÓN'), input('SECCIÓN'), input('TIPO DE PRODUCTO'))
        nuevo_producto = {
            'id': producto.id,
            'nombre': producto.nombre,
            'tipo': producto.tipo,
            'precio': producto.precio,
            'marca': producto.marca,
            'presentacion': producto.presentacion,
            'tamanio': producto.tamanio,
            'seccion': producto.seccion,
            'tipo_jabon': producto.tipo_jabon
        }

    elif opcion == 'Juguetes':
        print("JUGUETES: ")
        producto = Juguetes(input(' NOMBRE: '), 'Juguetes', int(input(' PRECIO: ')), input(' MARCA: '), input(' COLOR: '),int(input(' TAMAÑO: ')),input(' MATERIAL: '),int(input(' PESO:')))
        nuevo_producto = {
            'id': producto.id,
            'nombre': producto.nombre,
            'tipo': producto.tipo,
            'precio': producto.precio,
            'marca': producto.marca,
            'color': producto.color,
            'tamanio': producto.tamanio,
            'material': producto.material,
            'peso': producto.peso,
        }

    elif opcion == 'Vinos y licores':
        print("VINOS Y LICORES: ")
        producto = Vinos_y_licores(input(' NOMBRE: '), 'Vinos y licores', int(input(' PRECIO: ')), int(input(' CONTENIDO: ')), input(' SABOR: ')), int(input(' PORCENTAJE DE ALCOHOL: '))
        nuevo_producto = {
            'id': producto.id,
            'nombre': producto.nombre,
            'tipo': producto.tipo,
            'precio': producto.precio,
            'mililitros': producto.mililitros,
            'sabor': producto.sabor,
            'porcentaje': producto.porcentaje,
        }

    elif opcion == 'Panaderia':
        print("PANADERIA: ")
        producto = Panaderia(input(' NOMBRE: '), 'Panaderia', int(input(' PRECIO: ')), input(' MARCA: '), float(input(' PESO: ')), input(' CADUCIDAD: '), input(' TIPO DE PAN: '), input(' SABOR: '))
        nuevo_producto = {
            'id': producto.id,
            'nombre': producto.nombre,
            'tipo': producto.tipo,
            'precio': producto.precio,
            'marca': producto.marca,
            'peso': producto.peso,
            'caducidad': producto.caducidad,
            'tipo_pan': producto.tipo_de_pan,
            'sabor': producto.sabor,
        }

    elif opcion == 'Farmacia':
        print("FARMACIA: ")
        producto = Farmacia(input(' NOMBRE: '), 'Farmacia', int(input(' PRECIO: ')), int(input(' GRAMAJE: ')), int(input(' DOSIS: ')), input(' ENFERMEDAD: '), input(' TIPO: '), input(' CONTROLADO: '))
        nuevo_producto = {
            'id': producto.id,
            'nombre': producto.nombre,
            'tipo': producto.tipo,
            'precio': producto.precio,
            'gramaje': producto.gramaje,
            'dosis': producto.dosis,
            'enfermedad': producto.enfermedad,
            'tipo_medicamento': producto.tipo_medicamento,
            'controlado': producto.controlado,
        }

    return nuevo_producto
