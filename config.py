import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql+psycopg2://artesanato_user:123puc@localhost/artesanato_puc_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False