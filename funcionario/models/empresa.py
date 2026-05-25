class empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def mostrar_funcionarios(self):
        print(f"Funcionários da empresa {self.nome}:")
        for funcionario in self.funcionarios:
            funcionario.mostrar_informacoes()
            print()

    def folha_pagamento(self):
        for funcionario in self.funcionarios:
            pagamento = funcionario.calcular_pagamento()
            print(f"Pagamento de {funcionario.nome}: R$ {pagamento:.2f}")