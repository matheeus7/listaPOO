from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")

    @abstractmethod
    def calcular_pagamento(self):
        pass

    