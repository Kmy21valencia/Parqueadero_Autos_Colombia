from models.usuario import Usuario

class UsuarioController:
    def autenticar(self, nombre, contrasena):
        usuario = Usuario(None, nombre, None, contrasena)
        return usuario.autenticar(nombre, contrasena)