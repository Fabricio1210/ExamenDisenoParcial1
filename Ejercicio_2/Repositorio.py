class RepositorioBiblioteca: 
    def __init__(self, nombre_archivo="biblioteca.txt"):
        self.archivo = nombre_archivo
    
    def guardar_en_archivo(self, libros, prestamos):
        with open(self.archivo, 'w') as f:
            f.write(f"Libros: {len(libros)}\n")
            f.write(f"Préstamos: {len(prestamos)}\n")
    
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, 'r') as f:
                data = f.read()
            return True
        except:
            return False