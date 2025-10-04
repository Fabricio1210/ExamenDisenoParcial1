from abc import ABC, abstractmethod

# Aqui hacemos la interfaz del repositorio y debe ser abtracta para implementar los metodos luego

class IRepositorio(ABC): 
    def __init__(self, nombre_archivo="biblioteca.txt"):
        self.archivo = nombre_archivo
    
    @abstractmethod
    def guardar_en_archivo(self, libros, prestamos):
        pass
    
    @abstractmethod
    def cargar_desde_archivo(self):
        pass

# Extendemos de RepositorioArchivo lo cual nos obliga a implementar las clases lo cual nos deja implementar la logica que estaba desde un principio

class RepositorioBiblioteca(IRepositorio): 
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