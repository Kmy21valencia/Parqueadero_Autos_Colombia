class Celda:
    def __init__(self, numero, estado="libre"):
        self.numero = numero
        self.estado = estado

    def asignar_vehiculo(self, vehiculo):
        if self.estado == "libre":
            self.estado = "ocupada"
            print(f"Vehículo {vehiculo.placa} asignado a celda {self.numero}")
        else:
            print(f"Celda {self.numero} no está disponible")

    def liberar_celda(self):
        if self.estado == "ocupada":
            self.estado = "libre"
            print(f"Celda {self.numero} liberada")
        else:
            print(f"Celda {self.numero} ya está libre")