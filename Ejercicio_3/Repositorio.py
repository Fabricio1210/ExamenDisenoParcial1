from abc import ABC, abstractmethod

class RepositorioArchivo(ABC): 
    def __init__(self, nombre_archivo="biblioteca.txt"):
        self.archivo = nombre_archivo
    
    @abstractmethod
    def guardar_en_archivo(self, libros, prestamos):
        pass
    
    @abstractmethod
    def cargar_desde_archivo(self):
        pass

class RepositorioBiblioteca(RepositorioArchivo): 
    def __init__(self, nombre_archivo="biblioteca.txt"):
        super().__init__()
    
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