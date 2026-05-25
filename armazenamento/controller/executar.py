from typing import Any
from models.armazenador_abc import Armazenador
from models.armazenador_protocol import Salvavel


def executar_salvamento_formal(armazenador: Armazenador, dado: Any) -> None:
    if not isinstance(armazenador, Armazenador):
        raise TypeError(f"Objeto deve ser instância de Armazenador, "
                       f"recebido: {type(armazenador).__name__}")
    armazenador.salvar(dado)


def executar_salvamento_flexivel(objeto: Salvavel, dado: Any) -> None:
    if not hasattr(objeto, 'salvar') or not callable(getattr(objeto, 'salvar')):
        raise TypeError(f"Objeto deve implementar método 'salvar()', "
                       f"tipo recebido: {type(objeto).__name__}")
    objeto.salvar(dado)
