from models.funcionario import Funcionario

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, cpf, valor_hora, horas_trabalhadas):
        super().__init__(nome, cpf)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_pagamento(self):
        return self.valor_hora * self.horas_trabalhadas