from services.productos import Productos


class Farmacia(Productos):
    def __init__(self, nombre, tipo, precio, gramaje, dosis, enfermedad, tipo_medicamento, controlado):
        super().__init__(nombre, tipo, precio)
        self.gramaje = gramaje
        self.dosis = dosis
        self.enfermedad = enfermedad
        self.tipo_medicamento = tipo_medicamento
        self.controlado = controlado

    def __del__(self):
        pass

    @staticmethod
    def mostrar_datos(producto):
        Productos.mostrar_datos(producto)
        print ("GRAMAJE:  "+ str(producto['gramaje'])  + " gr\nDOSIS: "+ str(producto['dosis']) + "\nENFERMEDAD: " + producto['enfermedad'] + "\nTIPO: " + producto['tipo_medicamento'] + "\nCONTROLADO:" + producto['controlado'] + "")

    def push(self, array):
        nuevo_producto = {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'precio': self.precio,
            'gramaje': self.gramaje,
            'dosis': self.dosis,
            'enfermedad': self.enfermedad,
            'tipo_medicamento': self.tipo_medicamento,
            'controlado': self.controlado,
        }
        array.append(nuevo_producto)
