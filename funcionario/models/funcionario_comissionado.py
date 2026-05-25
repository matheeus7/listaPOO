from models.funcionario import Funcionario

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, cpf, valor_comissao, vendas_realizadas):
        super().__init__(nome, cpf)
        self.valor_comissao = valor_comissao
        self.vendas_realizadas = vendas_realizadas

    def calcular_pagamento(self):
        return self.valor_comissao * self.vendas_realizadas