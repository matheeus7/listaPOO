class centralNotificacao:
    def __init__(self):
        self.notificacoes = []


    def adicionar_notificacao(self, notificacao):
        self.notificacoes.append(notificacao)
        print("Notificação adicionada com sucesso.")

    def listar_notificacoes(self):
        print("Notificações cadastradas:")
        for notificacao in self.notificacoes:
            print(f"- {notificacao.__class__.__name__}")

    def enviar_todos(self, mensagem):
        print("Enviando mensagem para todas as notificações:")
        for notificacao in self.notificacoes:
            notificacao.enviar(mensagem)