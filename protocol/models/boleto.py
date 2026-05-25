class Boleto:
    def __init__(self, codigo, valor):
        self.codigo = codigo
        self.valor = valor
    
    def imprimir(self) -> None:
        print(f"╔════════════════════════════════════════╗")
        print(f"║         BOLETO BANCÁRIO               ║")
        print(f"║────────────────────────────────────────║")
        print(f"║ Código: {self.codigo:32s} ║")
        print(f"║ Valor:  R$ {self.valor:27.2f} ║")
        print(f"╚════════════════════════════════════════╝")
