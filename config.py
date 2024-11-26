import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URL não está definida! Certifique-se de que está configurada corretamente no ambiente do Render.")