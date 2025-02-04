from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import db
from datetime import datetime
from sqlalchemy.sql import expression

class Participants(UserMixin, db.Model):

    coordinator = db.Column(db.Boolean, server_default=expression.false())
    id = db.Column(db.Integer, primary_key=True)
    fortress = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    additional_info = db.Column(db.String(256))
    password_hash = db.Column(db.String(128))
    # password = db.Column(db.String(128), nullable=True)  # Hasło, które ustawia użytkownik
    # confirmed_at = db.Column(db.DateTime, nullable=True)  # Data potwierdzenia e-maila
    # created_at = db.Column(db.DateTime, default=datetime.utcnow)



# Plik definiuje modele bazy danych.
# W tym przypadku np. model Participant reprezentujący użytkowników aplikacji.