from flask import Blueprint

auth_bp = Blueprint('auth', __name__,template_folder='templates')

from app.auth.routes import auth_bp  # Importowanie routów

# Ten plik inicjalizuje blueprint auth_bp, który odpowiada za logikę autoryzacji.