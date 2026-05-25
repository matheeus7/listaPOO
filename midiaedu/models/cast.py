from models.midias import Midia

class Podcast (Midia):
    def __init__(self, titulo, duracao, apresentador):
        super().__init__(titulo, duracao)
        self.apresentador = apresentador

    def reproduzir(self):
        print(f"Reproduzindo: {self.titulo} | Duração: {self.duracao} | Apresentador: {self.apresentador} | ")