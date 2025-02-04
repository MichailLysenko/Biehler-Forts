# Generowanie tokenów
# Weryfikacja tokenów
# Inne pomocnicze operacje (np. manipulacja danymi, walidacja)

import jwt
from datetime import datetime, timedelta
from app.config import Config

def generate_confirmation_token(email):
    """
    Generuje token JWT do potwierdzenia e-maila.
    Token zawiera e-mail użytkownika oraz datę wygaśnięcia.
    """
    expiration_time = timedelta(hours=1)  # Token wygasa po godzinie
    payload = {
        'email': email,
        'exp': datetime.utcnow() + expiration_time  # Czas wygaśnięcia tokena
    }
    # Tworzymy token z payload i tajnym kluczem
    token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm='HS256')
    return token

def confirm_token(token):
    """
    Weryfikuje token JWT. Jeśli token jest prawidłowy, zwraca e-mail użytkownika.
    Jeśli token jest nieważny lub wygasł, zwraca None.
    """
    try:
        # Dekodowanie tokena i zwrócenie danych z niego (payload)
        payload = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=['HS256'])
        return payload['email']  # Zwracamy e-mail z tokena
    except jwt.ExpiredSignatureError:
        # Token wygasł
        return None
    except jwt.InvalidTokenError:
        # Token jest nieprawidłowy
        return None