from models.notificacao import Notificacao

class NotificarEmail(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando email com a mensagem: {mensagem}")