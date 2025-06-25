
from app.utils.planilha import buscar_dados_por_email
from app.services.octadesk_service import enviar_resposta

def processar_email(email, ticket_id):
    cliente = buscar_dados_por_email(email)

    if cliente:
        mensagem = (
            f"Olá {cliente['nome']}, encontramos seus dados:\n\n"
            f"🏠 Unidade: {cliente['unidade']}\n"
            f"📞 Telefone: {cliente['telefone']}"
        )
    else:
        mensagem = (
            "Desculpe, não localizamos esse e-mail em nossa base. "
            "Verifique se digitou corretamente."
        )

    return enviar_resposta(ticket_id, mensagem)
