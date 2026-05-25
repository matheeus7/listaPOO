class RelatorioSimples:
    def __init__(self, titulo: str):
        self.titulo = titulo
    
    def imprimir(self) -> None:
        print(f"╔════════════════════════════════════════╗")
        print(f"║          RELATÓRIO SIMPLES            ║")
        print(f"║────────────────────────────────────────║")
        print(f"║ Título: {self.titulo:<30} ║")
        print(f"╚════════════════════════════════════════╝")