# Esto es la clase que llevara todo lo que tenga que ver con notificadores y solo notificadores

class ServicioNotificaciones:
    def enviar_notificacion(self, usuario, libro):
        """Método _enviar_notificacion movido desde SistemaBiblioteca"""
        print(f"[NOTIFICACIÓN] {usuario}: Préstamo de '{libro}'")