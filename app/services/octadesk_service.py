
import requests
from app.config import Config

def enviar_resposta(ticket_id, mensagem):
    url = f"{Config.OCTA_BASE_URL}/tickets/{ticket_id}"
    headers = {
        "Authorization": f"Bearer {Config.OCTA_API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "content": mensagem,
        "type": "text",
        "channel": "whatsapp"
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)

        if 200 <= response.status_code < 300:
            print("✅ Mensagem enviada com sucesso")
            return True
        else:
            print(f"❌ Erro {response.status_code} na resposta da Octadesk:")
            print(response.text)
            return False

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao conectar com a API da Octadesk: {e}")
        return False


"""def enviar_resposta(ticket_id, mensagem):
    print("📦 Simulação de envio de mensagem para a Octadesk")
    print(f"🎫 Ticket ID: {ticket_id}")
    print(f"📩 Mensagem: {mensagem}")
    return True  # Simula sucesso
"""
