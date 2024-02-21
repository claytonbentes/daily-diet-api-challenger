from database import db
from flask_login import UserMixin
from datetime import datetime

class Refeicao(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False, unique=True)
    descricao = db.Column(db.String(100), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    dentro_dieta = db.Column(db.Boolean, nullable=False)