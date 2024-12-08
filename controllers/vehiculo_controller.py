from models.vehiculo import Vehiculo

class VehiculoController:
    def registrar_entrada(self, placa, marca, modelo, color):
        vehiculo = Vehiculo(placa, marca, modelo, color)
        vehiculo.registrar_entrada()

    def registrar_salida(self, placa):
        vehiculo = Vehiculo(placa, None, None, None)
        vehiculo.registrar_salida()