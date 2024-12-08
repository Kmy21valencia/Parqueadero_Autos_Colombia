import tkinter as tk
from tkinter import messagebox
from controllers.vehiculo_controller import VehiculoController
from controllers.celda_controller import CeldaController
from controllers.usuario_controller import UsuarioController
from controllers.registro_controller import RegistroController
from controllers.reporte_controller import ReporteController

class MainView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestión de Parqueadero - Autos Colombia")
        self.vehiculo_controller = VehiculoController()
        self.celda_controller = CeldaController()
        self.usuario_controller = UsuarioController()
        self.registro_controller = RegistroController()
        self.reporte_controller = ReporteController()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Gestión de Parqueadero", font=("Helvetica", 16)).pack(pady=10)

        tk.Button(self.root, text="Registrar Entrada", command=self.registrar_entrada).pack(pady=5)
        tk.Button(self.root, text="Registrar Salida", command=self.registrar_salida).pack(pady=5)
        tk.Button(self.root, text="Consultar Estado de Celdas", command=self.consultar_estado_celdas).pack(pady=5)
        tk.Button(self.root, text="Generar Reporte Diario", command=self.generar_reporte_diario).pack(pady=5)
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=5)

    def registrar_entrada(self):
        self.new_window("Registrar Entrada", self.registrar_entrada_action, ["Placa", "Marca", "Modelo", "Color"])

    def registrar_salida(self):
        self.new_window("Registrar Salida", self.registrar_salida_action, ["Placa"])

    def consultar_estado_celdas(self):
        messagebox.showinfo("Estado de Celdas", "Funcionalidad no implementada aún")

    def generar_reporte_diario(self):
        messagebox.showinfo("Reporte Diario", "Funcionalidad no implementada aún")

    def new_window(self, title, action, fields):
        window = tk.Toplevel(self.root)
        window.title(title)
        entries = {}
        for field in fields:
            tk.Label(window, text=f"{field}:").pack(pady=5)
            entry = tk.Entry(window)
            entry.pack(pady=5)
            entries[field] = entry
        tk.Button(window, text="Aceptar", command=lambda: action(entries)).pack(pady=5)

    def registrar_entrada_action(self, entries):
        placa = entries["Placa"].get()
        marca = entries["Marca"].get()
        modelo = entries["Modelo"].get()
        color = entries["Color"].get()
        self.vehiculo_controller.registrar_entrada(placa, marca, modelo, color)
        messagebox.showinfo("Registro de Entrada", f"Entrada registrada para vehículo {placa}")

    def registrar_salida_action(self, entries):
        placa = entries["Placa"].get()
        self.vehiculo_controller.registrar_salida(placa)
        messagebox.showinfo("Registro de Salida", f"Salida registrada para vehículo {placa}")

    def run(self):
        self.root.mainloop()