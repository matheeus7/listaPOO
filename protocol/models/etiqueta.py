class Etiqueta:
    def __init__(self, destinatario: str, endereco: str):
        self.destinatario = destinatario
        self.endereco = endereco
    
    def imprimir(self) -> None:
        print(f"╔════════════════════════════════════════╗")
        print(f"║          ETIQUETA DE ENTREGA          ║")
        print(f"║────────────────────────────────────────║")
        print(f"║ Para: {self.destinatario:28s} ║")
        print(f"║ Endereço:                            ║")
        print(f"║ {self.endereco:36s} ║")
        print(f"╚════════════════════════════════════════╝")
