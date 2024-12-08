from models.celda import Celda

class CeldaController:
    def asignar_vehiculo(self, numero, vehiculo):
        celda = Celda(numero)
        celda.asignar_vehiculo(vehiculo)

    def liberar_celda(self, numero):
        celda = Celda(numero)
        celda.liberar_celda()