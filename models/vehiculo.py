class Vehiculo:
    def __init__(self, placa, marca, modelo, color):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def registrar_entrada(self):
        print(f"Entrada registrada para vehículo {self.placa}")

    def registrar_salida(self):
        print(f"Salida registrada para vehículo {self.placa}")