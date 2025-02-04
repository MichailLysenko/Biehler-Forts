from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager, UserMixin
from app.models import Participants
from dotenv import load_dotenv
import os


migrate = Migrate()
mail = Mail()
login_manager = LoginManager()

# Opcjonalne ustawienia LoginManager
login_manager.login_view = "auth.login"  # Przekierowanie na login, jeśli użytkownik niezalogowany
login_manager.login_message = "Zaloguj się, aby uzyskać dostęp."

@login_manager.user_loader
def load_user(user_email):
    # Jeśli email to koordynator, zwróć instancję klasy User
    print(user_email)

    # W przeciwnym razie szukaj w bazie uczestników
    participant = Participants.query.filter_by(id=user_email).first()
    if participant:
        return participant

    return None

# Ten plik zawiera inicjalizację rozszerzeń używanych w aplikacji,
# takich jak SQLAlchemy, Mail, Flask-Migrate czy LoginManager.
# Umieszczanie ich tutaj pomaga utrzymać porządek.