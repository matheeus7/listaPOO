from models.notificar_email import NotificarEmail
from models.notificar_sms import NotificarSMS
from models.notificar_app import NotificarAPP
from models.centralnotificacao import centralNotificacao

if __name__ == "__main__":
    central = centralNotificacao()



    email_notificacao = NotificarEmail()
    sms_notificacao = NotificarSMS()
    app_notificacao = NotificarAPP()

    central.adicionar_notificacao(email_notificacao)
    central.adicionar_notificacao(sms_notificacao)
    central.adicionar_notificacao(app_notificacao)

    central.listar_notificacoes()

    central.enviar_todos("Esta é uma mensagem de teste para todas as notificações.")