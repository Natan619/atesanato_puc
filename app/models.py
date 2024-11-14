from . import db
from datetime import datetime

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    faturamento = db.Column(db.Float, nullable=False)  
    forma_pagamento = db.Column(db.String(50), nullable=False)
    data = db.Column(db.Date, nullable=False, default=datetime.utcnow)  

class Artesanato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    faturamento = db.Column(db.Float, nullable=False)
    forma_pagamento = db.Column(db.String(50), nullable=False)
    data = db.Column(db.Date, nullable=False, default=datetime.utcnow)  

class Gasto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_do_gasto = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)  
    forma_pagamento = db.Column(db.String(50), nullable=False)
    data = db.Column(db.Date, nullable=False, default=datetime.utcnow)