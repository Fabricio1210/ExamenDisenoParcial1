# Dividimos responsabilidades y esta le toca la clase de notificacion

class ServicioNotificaciones:
    def enviar_notificacion(self, usuario, libro):
        """Método _enviar_notificacion movido desde SistemaBiblioteca"""
        print(f"[NOTIFICACIÓN] {usuario}: Préstamo de '{libro}'")