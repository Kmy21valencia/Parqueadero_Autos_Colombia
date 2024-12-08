from models.registro_entrada import RegistroEntrada
from models.registro_salida import RegistroSalida

class RegistroController:
    def crear_registro_entrada(self, id_registro, fecha_hora_entrada, placa_vehiculo, id_usuario, numero_celda):
        registro = RegistroEntrada(id_registro, fecha_hora_entrada, placa_vehiculo, id_usuario, numero_celda)
        registro.crear_registro_entrada()

    def crear_registro_salida(self, id_registro, fecha_hora_salida, placa_vehiculo, id_usuario, numero_celda):
        registro = RegistroSalida(id_registro, fecha_hora_salida, placa_vehiculo, id_usuario, numero_celda)
        registro.crear_registro_salida()