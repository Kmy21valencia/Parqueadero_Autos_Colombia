class Reporte:
    def __init__(self, id_reporte, fecha_generacion, tipo_reporte):
        self.id_reporte = id_reporte
        self.fecha_generacion = fecha_generacion
        self.tipo_reporte = tipo_reporte

    def generar_reporte_diario(self):
        print("Reporte diario generado")

    def generar_reporte_mensual(self):
        print("Reporte mensual generado")