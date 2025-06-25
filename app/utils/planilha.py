
import pandas as pd
from app.config import Config

def buscar_dados_por_email(email_usuario):
    df = pd.read_excel(Config.BASE_CLIENTES_PATH)
    df['email'] = df['email'].str.lower()
    resultado = df[df["email"] == email_usuario.lower()]

    if resultado.empty:
        return None
    return resultado.iloc[0].to_dict()
