from abc import ABC, abstractmethod
from typing import List

# Basicamente aqui lo que hacemos es segregar la busqueda en diferentes tipos de
# busqueda para que cuando lo llamemos en el principal solo mande a llamar busqueda
# y por polimorfismo agarre el metodo que necesitemos filtrar ya sea por autor o 
# algo asi tambien vendria usando el principio open close ya que esta abierto para
# aumentar criterios de filtrado pero cerrado para su codigo en el main

class Busqueda(ABC):
    @abstractmethod
    def buscar(self, valor: str, libros: list):
        pass 

class BusquedaTitulo(Busqueda):
    def buscar(self, valor: str, libros: list):
        coincidencias = []
        for libro in libros:
            if valor.lower() in libro.titulo.lower():
                coincidencias.append(libro)
        return coincidencias;

class BusquedaAuthor(Busqueda):
    def buscar(self, valor: str, libros: list):
        coincidencias = []
        for libro in libros:
            if valor.lower() in libro.autor.lower():
                coincidencias.append(libro)
        return coincidencias;

class BusquedaISBN(Busqueda):
    def buscar(self, valor: str, libros: list):
        coincidencias = []
        for libro in libros:
            if valor.lower() in libro.isbn.lower():
                coincidencias.append(libro)
        return coincidencias;        

class BusquedaDisponibilidad(Busqueda):
    def buscar(self, valor: str, libros: list):
        coincidencias = []
        disponible = valor.lower() == "true"
        for libro in libros:
            if libro.disponible == disponible:
                coincidencias.append(libro)
        return coincidencias;