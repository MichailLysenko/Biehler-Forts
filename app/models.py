from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import db
from datetime import datetime
from sqlalchemy.sql import expression
from itsdangerous import URLSafeTimedSerializer as Serializer, URLSafeTimedSerializer
#from app.config import Config #zeby wszedl do app.config
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

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

    def generate_reset_token(self):
        s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return s.dumps(self.email, salt="reset-password")

    @staticmethod
    def verify_token(token, expiration=3600):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            email = serializer.loads(token, salt='reset-password', max_age=expiration)
            return email
        except:
            return None



