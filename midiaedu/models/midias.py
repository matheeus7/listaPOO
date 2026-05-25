from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao
    
    def info(self):
        print(f"Titulo: {self.titulo} | Duração: {self.duracao}")

    @abstractmethod
    def reproduzir (self):
        pass