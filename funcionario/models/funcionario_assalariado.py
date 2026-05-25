from models.funcionario import Funcionario


class FuncionarioAssalariado(Funcionario):
    def __init__(self, nome, cpf, salario_mensal):
        super().__init__(nome, cpf)
        self.salario_mensal = salario_mensal

    def calcular_pagamento(self):
        return self.salario_mensal