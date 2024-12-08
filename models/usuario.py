class Usuario:
    def __init__(self, id_usuario, nombre, tipo, contrasena):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.tipo = tipo
        self.contrasena = contrasena

    def autenticar(self, nombre, contrasena):
        if self.nombre == nombre and self.contrasena == contrasena:
            print(f"Usuario {self.nombre} autenticado")
            return True
        else:
            print("Credenciales incorrectas")
            return False