from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.imprimivel import Imprimivel


def processar_impressao(item: "Imprimivel") -> None:
    """
    Processa a impressão de um item compatível com o protocolo Imprimivel.
    
    Esta função demonstra o uso de Protocols: aceita qualquer objeto que
    implemente o método imprimir(), sem necessidade de herança.
    
    Args:
        item: Qualquer objeto que implemente o protocolo Imprimivel
    """
    print("\n[Iniciando processo de impressão...]")
    item.imprimir()
    print("[Processo de impressão concluído!]\n")
