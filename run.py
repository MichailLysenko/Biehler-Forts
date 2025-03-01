from flask import Flask
from flask_mail import Mail
from app.db import db
from app.extensions import migrate, mail, login_manager
from app.models import Participants
from app.config import Config
from app.auth import auth_bp
from app.main import main_bp
import sys
import os

def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'app', 'templates'))
    app.config.from_object("app.config.Config")
    database_location = "sqlite:///C:\\Users\\biehl\\PycharmProjects\\TestProject\\venv\\Biehler-Forts\\database.db"
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'defaultsecretkey')  # Default if not found
    app.config['SQLALCHEMY_DATABASE_URI'] = database_location
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAIL_SERVER'] = 'smtp-relay.brevo.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    mail = Mail(app)

    # Inicjalizacja rozszerzeń
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    login_manager.init_app(app)

    # Konfiguracja Flask-Login
    login_manager.login_view = "auth.login"  # Nazwa endpointu logowania
    login_manager.login_message = "Proszę się zalogować, aby uzyskać dostęp do tej strony."
    login_manager.login_message_category = "info"

    # Rejestracja blueprintów
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp)


    return app

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)