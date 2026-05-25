from typing import Any
from models.armazenador_abc import ArmazenadorArquivo, ArmazenadorBanco
from models.armazenador_protocol import ArmazenadorNuvem
from controller.executar import executar_salvamento_formal, executar_salvamento_flexivel


def main():
    print("=" * 70)
    print("COMPARAÇÃO: ABC vs Protocol")
    print("=" * 70)
    
    arquivo = ArmazenadorArquivo("dados_locais.txt")
    banco = ArmazenadorBanco("dados.db")
    nuvem = ArmazenadorNuvem("usuario@gmail.com")
    
    dados_teste = [
        "Usuário João criado",
        "Transação de R$ 100,00",
        "Relatório mensal gerado"
    ]
    
    print("\n" + "─" * 70)
    print("PARTE A - Abordagem Formal (ABC)")
    print("─" * 70)
    
    print("\n1. Testando executar_salvamento_formal():")
    print("\nArmazenador de Arquivo:")
    executar_salvamento_formal(arquivo, dados_teste[0])
    
    print("\nArmazenador de Banco de Dados:")
    executar_salvamento_formal(banco, dados_teste[0])
    
    print("\nTentando salvar com ArmazenadorNuvem (esperado: erro):")
    try:
        executar_salvamento_formal(nuvem, dados_teste[0])
    except TypeError as e:
        print(f"✗ Erro esperado: {e}")
    
    print("\n" + "─" * 70)
    print("PARTE B - Abordagem Flexível (Protocol)")
    print("─" * 70)
    
    print("\n2. Testando executar_salvamento_flexivel():")
    print("\nArmazenador de Arquivo:")
    executar_salvamento_flexivel(arquivo, dados_teste[1])
    
    print("\nArmazenador de Banco de Dados:")
    executar_salvamento_flexivel(banco, dados_teste[1])
    
    print("\nArmazenador de Nuvem:")
    executar_salvamento_flexivel(nuvem, dados_teste[1])
    
    print("\n" + "─" * 70)
    print("TESTES ADICIONAIS")
    print("─" * 70)
    
    print("\n3. Testando com múltiplos dados (abordagem flexível):")
    for dado in dados_teste[2:]:
        print(f"\nSalvando: '{dado}'")
        executar_salvamento_flexivel(arquivo, dado)
        executar_salvamento_flexivel(banco, dado)
        executar_salvamento_flexivel(nuvem, dado)
    
    print("\n" + "─" * 70)
    print("DADOS ARMAZENADOS")
    print("─" * 70)
    
    print("\nDados no Banco de Dados:")
    banco.listar()
    
    print("\nDados na Nuvem:")
    nuvem.listar()
    
    print("\n" + "─" * 70)
    print("CLASSE CUSTOMIZADA COM PROTOCOL")
    print("─" * 70)
    
    class ArmazenadorCSV:
        def __init__(self, arquivo: str = "dados.csv"):
            self.arquivo = arquivo
            self.dados = []
        
        def salvar(self, dado: Any) -> None:
            self.dados.append(dado)
            print(f"✓ CSV: Dado salvo em '{self.arquivo}'")
    
    csv = ArmazenadorCSV()
    
    print("\n4. Testando classe customizada com executar_salvamento_flexivel():")
    for dado in dados_teste:
        executar_salvamento_flexivel(csv, dado)
    
    print("\n5. Tentando usar classe customizada com executar_salvamento_formal():")
    try:
        executar_salvamento_formal(csv, "teste")
    except TypeError as e:
        print(f"✗ Erro esperado: {e}")
    
    print("\n" + "=" * 70)
    print("RESUMO COMPARATIVO")
    print("=" * 70)
    
    resumo = """
    ABC (Abstract Base Class):
      ✓ Contrato formal explícito
      ✓ Hierarquia clara
      ✓ Verificação em tempo de código
      ✗ Requer herança obrigatória
      ✗ Menos flexível
    
    Protocol (Duck Typing):
      ✓ Altamente flexível
      ✓ Sem herança obrigatória
      ✓ Melhor para integração externa
      ✗ Contrato menos explícito
      ✗ Erros em tempo de execução
    
    Quando usar ABC:
      - Projeto com hierarquia clara e controlada
      - Quando você quer impor herança
      - APIs internas bem definidas
    
    Quando usar Protocol:
      - Máxima flexibilidade necessária
      - Integração com código externo
      - Quando o "como" é menos importante que "o quê"
    """
    
    print(resumo)


if __name__ == "__main__":
    main()
