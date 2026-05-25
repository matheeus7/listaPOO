from models.notificacao import Notificacao

class NotificarSMS(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando SMS com a mensagem: {mensagem}")