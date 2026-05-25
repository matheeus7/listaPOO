from typing import Protocol, Any
from datetime import datetime


class Salvavel(Protocol):
    def salvar(self, dado: Any) -> None:
        ...


class ArmazenadorNuvem:
    def __init__(self, usuario: str = "usuario@nuvem.com"):
        self.usuario = usuario
        self.dados = []
    
    def salvar(self, dado: Any) -> None:
        registro = {
            'usuario': self.usuario,
            'dado': dado,
            'timestamp': datetime.now().isoformat()
        }
        self.dados.append(registro)
        print(f"✓ Nuvem: Dado salvo para usuário '{self.usuario}'")
    
    def listar(self) -> None:
        if not self.dados:
            print("  (nuvem vazia)")
            return
        for registro in self.dados:
            print(f"  {registro['usuario']}: {registro['dado']} - {registro['timestamp']}")
