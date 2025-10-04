# Esta clase nos ayuda a validar todos los objetos que hay quye validar

class ValidadorBiblioteca:
    def validar_libro(self, titulo, autor, isbn):
        if not titulo or len(titulo) < 2:
            return "Error: Título inválido"
        if not autor or len(autor) < 3:
            return "Error: Autor inválido"
        if not isbn or len(isbn) < 10:
            return "Error: ISBN inválido"
        return None
    
    def validar_usuario(self, usuario):
        if not usuario or len(usuario) < 3:
            return "Error: Nombre de usuario inválido"
        return None
    