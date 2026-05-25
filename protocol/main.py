from models.boleto import Boleto
from models.etiqueta import Etiqueta
from models.relatorio import RelatorioSimples
from controller.impressao import processar_impressao


def main():
    print("=" * 40)
    print("DEMONSTRAÇÃO DE PROTOCOL IMPRIMIVEL")
    print("=" * 40)
    boleto = Boleto(codigo="12345.67890 98765.432109", valor=150.00)
    etiqueta = Etiqueta(
        destinatario="João Silva",
        endereco="Rua das Flores, 123 - SP"
    )
    relatorio = RelatorioSimples(titulo="Relatório de Vendas")

    processar_impressao(boleto)
    processar_impressao(etiqueta)
    processar_impressao(relatorio)

if __name__ == "__main__":
    main()
