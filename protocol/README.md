# Protocol Imprimível - Exercício de Contrato Estrutural

## Descrição

Este projeto demonstra o uso de **Protocols** em Python para criar um contrato estrutural sem exigir herança obrigatória. Diferentes tipos de objetos (Boleto, Etiqueta, RelatorioSimples) implementam o protocolo `Imprimivel` e podem ser processados pela função `processar_impressao()`.

## Estrutura do Projeto

```
protocol/
├── models/
│   ├── __init__.py
│   ├── imprimivel.py        # Protocol Imprimivel
│   ├── boleto.py            # Classe Boleto
│   ├── etiqueta.py          # Classe Etiqueta
│   └── relatorio.py         # Classe RelatorioSimples
├── controller/
│   ├── __init__.py
│   └── impressao.py         # Função processar_impressao()
└── main.py                  # Demonstração
```

## Componentes

### 1. **Protocol Imprimivel** (`models/imprimivel.py`)

Define o contrato que todos os objetos imprimíveis devem seguir:

```python
class Imprimivel(Protocol):
    def imprimir(self) -> None:
        ...
```

**Vantagem**: Qualquer classe que implemente `imprimir()` é compatível, sem necessidade de herança.

### 2. **Classes Implementadoras**

#### Boleto (`models/boleto.py`)
- **Atributos**: `codigo`, `valor`
- **Método**: `imprimir()`

#### Etiqueta (`models/etiqueta.py`)
- **Atributos**: `destinatario`, `endereco`
- **Método**: `imprimir()`

#### RelatorioSimples (`models/relatorio.py`)
- **Atributo**: `titulo`
- **Método**: `imprimir()`

### 3. **Função Processadora** (`controller/impressao.py`)

```python
def processar_impressao(item: "Imprimivel") -> None:
    """Processa a impressão de um item compatível com o protocolo Imprimivel."""
    item.imprimir()
```

Aceita qualquer objeto que implemente o protocolo, sem tipo específico.

## Como Executar

```bash
python main.py
```

## Vantagens do Protocol

| Aspecto | Sem Protocol | Com Protocol |
|--------|------------|------------|
| Herança | Obrigatória | Opcional |
| Compatibilidade | Rígida | Flexível |
| Duck Typing | Sem verificação de tipo | Com type hints |
| Novo tipo | Precisa herdar | Só implementar método |

## Conceitos-Chave

- **Protocol**: Define uma interface implícita (contrato estrutural)
- **Duck Typing**: "Se caminha como um pato e grasna como um pato, é um pato"
- **Type Hints**: Melhoram a clareza do código sem alterar o comportamento em runtime
- **Coesão**: Classes independentes, mas com contrato comum

## Requisitos

- Python 3.8+
- Módulo `typing` (incluído na stdlib)

## Autor

Exercício de Estrutura de Dados - Lista II
