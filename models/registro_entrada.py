class RegistroEntrada:
    def __init__(self, id_registro, fecha_hora_entrada, placa_vehiculo, id_usuario, numero_celda):
        self.id_registro = id_registro
        self.fecha_hora_entrada = fecha_hora_entrada
        self.placa_vehiculo = placa_vehiculo
        self.id_usuario = id_usuario
        self.numero_celda = numero_celda

    def crear_registro_entrada(self):
        print(f"Registro de entrada creado para vehículo {self.placa_vehiculo} en celda {self.numero_celda}")