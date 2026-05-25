from abc import ABC, abstractmethod
from typing import Any
from datetime import datetime


class Armazenador(ABC):
    @abstractmethod
    def salvar(self, dado: Any) -> None:
        pass


class ArmazenadorArquivo(Armazenador):
    def __init__(self, caminho: str = "dados.txt"):
        self.caminho = caminho
    
    def salvar(self, dado: Any) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.caminho, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {dado}\n")
        print(f"✓ Arquivo: Dado salvo em '{self.caminho}'")


class ArmazenadorBanco(Armazenador):
    def __init__(self, nome_banco: str = "dados.db"):
        self.nome_banco = nome_banco
        self.dados = []
    
    def salvar(self, dado: Any) -> None:
        registro = {
            'id': len(self.dados) + 1,
            'dado': dado,
            'timestamp': datetime.now().isoformat()
        }
        self.dados.append(registro)
        print(f"✓ Banco: Dado salvo (ID: {registro['id']}) em '{self.nome_banco}'")
    
    def listar(self) -> None:
        if not self.dados:
            print("  (banco vazio)")
            return
        for registro in self.dados:
            print(f"  ID {registro['id']}: {registro['dado']} - {registro['timestamp']}")
