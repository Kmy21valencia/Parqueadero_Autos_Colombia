from models.reporte import Reporte

class ReporteController:
    def generar_reporte_diario(self, id_reporte, fecha_generacion):
        reporte = Reporte(id_reporte, fecha_generacion, "diario")
        reporte.generar_reporte_diario()

    def generar_reporte_mensual(self, id_reporte, fecha_generacion):
        reporte = Reporte(id_reporte, fecha_generacion, "mensual")
        reporte.generar_reporte_mensual()