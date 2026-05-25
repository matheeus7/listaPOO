from models.funcionario_assalariado import FuncionarioAssalariado
from models.funcionario_comissionado import FuncionarioComissionado
from models.funcionario_horista import FuncionarioHorista
from models.empresa import empresa

empresa1 = empresa("Tech Solutions")

funcionario1 = FuncionarioAssalariado("Alice", "123.456.789-00", 3000)
funcionario2 = FuncionarioHorista("Bob", "987.654.321-00", 20, 160)
funcionario3 = FuncionarioComissionado("Charlie", "555.666.777-00", 50, 30)

empresa1.adicionar_funcionario(funcionario1)
empresa1.adicionar_funcionario(funcionario2)
empresa1.adicionar_funcionario(funcionario3)

empresa1.mostrar_funcionarios()

print("Folha de pagamento:")
empresa1.folha_pagamento()