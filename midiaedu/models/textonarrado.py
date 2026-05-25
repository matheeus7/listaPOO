from models.midias import Midia

class TextoNarrado (Midia):
    def __init__(self, titulo, duracao, idioma):
        super().__init__(titulo, duracao)
        self.idioma = idioma

    def reproduzir(self):
        print(f"Reproduzindo: {self.titulo} | duração: {self.duracao} minutos | Idioma: {self.idioma}" )

