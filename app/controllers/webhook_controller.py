
from flask import Blueprint, request, jsonify
from app.services.cliente_service import processar_email

webhook_bp = Blueprint("webhook", __name__)

@webhook_bp.route("/", methods=["POST"])
def receber_webhook():
    dados = request.json

    if not dados or "text" not in dados or "ticketId" not in dados:
        return jsonify({"error": "Dados inválidos"}), 400

    email = dados["text"].strip()
    ticket_id = dados["ticketId"]

    sucesso = processar_email(email, ticket_id)

    if sucesso:
        return jsonify({"status": "Mensagem enviada com sucesso"}), 200
    else:
        return jsonify({"status": "Erro ao responder"}), 500
