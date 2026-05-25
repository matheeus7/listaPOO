from models.midias import Midia

class Plataformas:
    def __init__(self, nome):
        self.nome = nome
        self.lista = []

    def adicionar_midia(self, midia):
        self.lista.append(midia)

    def listar_midias(self):
        print(f"------------- Listando mídias: {self.nome} --------------")
        for midia in self.lista:
            midia.info()

    def reproduzir_todas_midias(self):
        print(f"-------------- Reproduzindo todas as mídias da plataforma: {self.nome} -----------------")
        for midia in self.lista:
            midia.reproduzir()
