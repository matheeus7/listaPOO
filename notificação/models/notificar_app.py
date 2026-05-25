from models.notificacao import Notificacao

class NotificarAPP(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando notificação no app com a mensagem: {mensagem}")