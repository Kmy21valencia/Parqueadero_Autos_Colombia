class RegistroSalida:
    def __init__(self, id_registro, fecha_hora_salida, placa_vehiculo, id_usuario, numero_celda):
        self.id_registro = id_registro
        self.fecha_hora_salida = fecha_hora_salida
        self.placa_vehiculo = placa_vehiculo
        self.id_usuario = id_usuario
        self.numero_celda = numero_celda

    def crear_registro_salida(self):
        print(f"Registro de salida creado para vehículo {self.placa_vehiculo} de celda {self.numero_celda}")