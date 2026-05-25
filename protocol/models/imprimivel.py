from typing import Protocol


class Imprimivel(Protocol):
    def imprimir(self) -> None:
        ...