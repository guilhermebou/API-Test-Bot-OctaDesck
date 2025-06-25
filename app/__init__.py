
from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    app = Flask(__name__)

    from app.controllers.webhook_controller import webhook_bp
    app.register_blueprint(webhook_bp, url_prefix="/webhook")

    return app
