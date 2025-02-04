
#*** updated
# 1. Należy utworzyć menu główne, w którym wprowadzić nagłówek
#   „Biehler-Forts: Historia i wspólczesne użytkowanie”.
# 2. Menu główne musi być również zaopatrzone w obraz -
#   logo_biehler_przezr. - który znajduję się pod napisem nagłówka.
#   Obraz pod tą nazwą przychowany jest w folderze static.
# 3. Czciąka nagłówków, pzycisków, rozmiar obrazu muszą być dopasowane do siebie,
#   żeby być przyjaznymi dla oczu użytkownika
# 4. Jest to strona o tematyce fortecznej, tak że css może być w odpowiednich
#   odcieniach i barwach.
# 5. W menu głównym, pod obrazem, muszą znajdować się przyciski,
#   które umożliwiają przejście do poszczególnych formularzy.
# 6. Pod przyciskami znajdują się dodatkowe informacje (opcjonalnie).
#   Przyciski w menu głównym to są: "O nas" (dodatek- "nasza działalnośc"),
#   "Login" ("dla tych, kto już bierzę udział"),
# 7. Przycisk "O nas" prowadzi do strony html, która będzie wyświetlać tekst: ...
#   Na końcu strony, po zakończeniu dodac przycisk "Do menu głównego"
# 8. Przycisk "Login" prowadzi do formularza rejestracji. Pojawiają się 2 pola:
#   login (z dodatkiem komentarza "twoj mail"), hasło i przycisk "wyślij".
#   Musi w tym formularzu być zachowany warunek - podane maile muszą już
#   znajdować sie w bazie danych "uczestnicy". Hasło musi być dobrze zabezpieczone.
# 9. Po logowaniu użytkownik przychodzi do formularza html o nazwie
#   "zgoda na udostępnianie danych (imię, nazwisko, mail, fort) dla wszystkich
#   dotychczas zarejestrowanych uczestników projektu w celu skutecznej integracji
#   i kooperacji".
# 10. Na końcu tej klauzuli muszą znajdować się dwa przyciski: "Zgadzam się"
#   oraz "Nie zgadzam się"
# 11. Przycisk "Zgadzam się" prowadzi do formularza strony bazy danych SQLite,
#   opartej na pliku "participants.db" (tu zamiast - dddatabase.html)
#   zawierającej informacje w kolumnach: „Twierdza”, „Imię”, „Nazwisko”,
#   „E-mail”, „Numer telefonu”. Na tej stronie na dole znajduję się przycisk
#   "Wyjśc", prowadzący na stronę główną i powodujący wylogowanie użytkownika.
# 12. Przycisk "Nie zgadzam się" wyprowadza na stronę główną i powoduję usunięcie
#   maila użytkownika z bazy danych.
# 13. Przy "Login" musi wystąpić jeszcze jeden wyjątek. Adres b.e......o...@...
#   z hasłem "W...@." musi być rozpoznawany jako login koordynatora. Ten sposób
#   logowania prowadzi do formularza "Koordynacja" - dostępnej tylko pod tym
#   loginem i hasłem. Jeżeli ma nastąpić błędne hasło, to należy wysłać
#   powiadomienie na maila koordynatora o możliwości zmiany hasła.
# 14. Formularz "Koordynacja" musi zawierać pola: „Twierdza”, „Imię”, „Nazwisko”,
#   „E-mail”, „Numer telefonu”. Na końcu strony znajduję się przyciski
#   "Na stronę główną" oraz "Wysłać". Przy użyciu "Wysłać" wprowadzone dane
#   powinni trafić do bazy danych. Po wysłaniu - powrót do formularza
#   "Koordynacja". Przycisk "Na stronę główną" prowadzi na stronę główną.
# 15. Przycisk "Rejestracja" prowadzi do formularza z polami „Twierdza”, „Imię”,
#   „Nazwisko”, „E-mail”, „Numer telefonu”, "Dodatkowe informacje (opcjonalnie)"
# 16. Na końcu formularza - przyciski "wyślij" i "na stronę główną" - w ten sposób
#   ma przyjść powiadomienie z danymi o próbie rejestracji na maila koordynatora
#   z opcją potwierdzenia zgłoszenia. Po potwierdzeniu zgłoszenia dane trafiają
#   do bazy danych.
# 17. Po użyciu przycisku "wyślij" użytkownik jest przekierowywany na stronę główną.
#   To samo się dzieję w przypadku użycia przycisku "na stronę główną".
# 18. Cała ta informacja ma być w języku Angielskim.
# Dodatkowo:
# 19. Na formularzu "O nas" o górze mają znajdować się przyciski przekierowujące
#   na strony zewnętrzne: do grupy na Facebook, go Funpage na Facebook oraz do
#   wymienionych stron internetowych: ...
# 20. Na formularzach koordynatora oraz login (zarejestrowanych użytkowników) muszą
#   działać funkcjonalnosci: 1) przy kliknięciu w adres mailowy można napisać i
#   wysłać wiadomosć na wybrany adres, 2) ma być możliwosć wysłania wiadomosci dla
#   wszystkich uczetników.

# 21. Przy rejestracji na stronie formularza "Coordination" na
#   maila uczestnika oraz na adres "biehler.forts@gmail.com" ma trafić powiadomienie
#   "Przeprowadzono rejestracje na stronie Biehler Forts (link do strony). Haslo
#   zostało nadane automatycznie. Proszę wejsc na strone i zmienic hasło na oryginalne.

# 22. Na stronie głównej musi być zaimplementowana funksjonalnosć tłumaczenia całej
#   tresci stron danej api z języka Angielskiego na język Polski, Niemiecki,
#   Francuski, Rosyjski.

# ***
# project/
# ├── app/                # Główna aplikacja Flaska
# │   ├── __init__.py     # Inicjalizacja aplikacji Flask i jej rozszerzeń
# │   ├── extensions.py   # Rejestracja i konfiguracja rozszerzeń Flaska
# │   ├── models.py       # Modele baz danych
# │   ├── auth/           # Moduł odpowiedzialny za autoryzację użytkowników
# │   │   ├── __init__.py
# │   │   ├── routes.py   # Logika logowania, wylogowania, rejestracji, resetu hasła
# │   ├── main/           # Moduł dla funkcji ogólnych (strona główna, profile)
# │   │   ├── __init__.py
# │   │   ├── routes.py   # Logika wyświetlania strony głównej, profilu użytkownika
# │   ├── email.py        # Logika wysyłania e-maili
# │   ├── utils.py        # Funkcje pomocnicze (np. generowanie tokenów)
# │   ├── config.py       # Konfiguracja aplikacji (np. środowisko, bazy danych)
# ├── migrations/         # Pliki migracji bazy danych (utworzone przez Flask-Migrate)
# ├── run.py              # Główny plik uruchamiający aplikację Flask
# └── requirements.txt    # Lista zależności projektu

# from flask import Flask, Blueprint, render_template, redirect, request, url_for, flash, session
# #import sqlite3
# import json
# from dotenv import load_dotenv
# import os
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase
# from flask_migrate import Migrate
# from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
# from flask_mail import Mail, Message
# from flask_googletrans import translator
# from itsdangerous import URLSafeTimedSerializer
# from sqlalchemy.sql import expression
# from auth import auth
# import requests
# import secrets
# import string
# # from app import db, Participants # dla dalszego usuwania danych
#
# # from flask_wtf import FlaskForm
# # from wtforms import StringField, PasswordField
# # from wtforms.validators import DataRequired, Email, Length
#
#
#
# load_dotenv()
#
# app = Flask(__name__)
# ts = translator(app)
# #translator.init_app(app)
# database_location = "sqlite:///C:\\Users\\biehl\\PycharmProjects\\TestProject\\venv\\Biehler-Forts\\database.db"
#
# # Konfiguracja bazy danych (SQLite for development)
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'defaultsecretkey')  # Default if not found
# app.config['SQLALCHEMY_DATABASE_URI'] = database_location
# #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['MAIL_SERVER'] = 'smtp.yourmailserver.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
# mail = Mail(app)
#
# # Inicjalizacja bazy danych i migracji
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
#
# coordinator_email = os.getenv('COORDINATOR_EMAIL')
# coordinator_password = os.getenv('COORDINATOR_PASSWORD')
#
#
# auth = Blueprint('auth', __name__)
# main = Blueprint('main', __name__)
#
# app.register_blueprint(auth)
# app.register_blueprint(main)
#
# login_manager = LoginManager()
# login_manager.login_view = 'auth.login'
# login_manager.init_app(app)
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     # since the user_id is just the primary key of our user table, use it in the query for the user
#     return Participants.query.get(int(user_id))
#
#
# class Participants(UserMixin, db.Model):
#
#     coordinator = db.Column(db.Boolean, server_default=expression.false())
#     id = db.Column(db.Integer, primary_key=True)
#     fortress = db.Column(db.String(100), nullable=False)
#     first_name = db.Column(db.String(100), nullable=False)
#     last_name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     phone_number = db.Column(db.String(20))
#     additional_info = db.Column(db.String(256))
#     password_hash = db.Column(db.String(128))
#
#     def __init__(self, fortress, first_name, last_name, email, phone_number, additional_info, password_hash):
#         self.fortress = fortress
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.phone_number = phone_number
#         self.additional_info = additional_info
#         self.password_hash = generate_password_hash(password_hash)
#
# with app.app_context():
#     db.create_all()
#
# @main.route('/profile')
# @login_required
# def profile():
#     return render_template('profile.html', name=current_user.email)
#
# @auth.route('/login', methods=['POST'])
# def login_post():
#     # login code goes here
#     email = request.form.get('email')
#     password = request.form.get('password')
#     remember = True if request.form.get('remember') else False
#
#     user = User.query.filter_by(email=email).first()
#
#     # check if the user actually exists
#     # take the user-supplied password, hash it, and compare it to the hashed password in the database
#     if not user or not check_password_hash(user.password, password):
#         flash('Please check your login details and try again.')
#         return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
#
#     # if the above check passes, then we know the user has the right credentials
#     return redirect(url_for('main.profile'))
#
#     login_user(user, remember=remember)
#     return redirect(url_for('main.profile'))
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/about')
# def about():
#     return render_template('about.html')
#
# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('main.index'))
#
# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         email = request.form['email']
# #         password = request.form['password']
# #         user = Participants.query.filter_by(email=email).first()
# #
# #         if email == coordinator_email:
# #             if password == coordinator_password:
# #                 session['coordinator'] = True
# #                 return redirect(url_for('coordination'))
# #             else:
# #                 flash('Incorrect password. An email was sent to the coordinator to reset the password.')
# #                 # Wyślij powiadomienie e-mail do koordynatora o błędnym haśle (implementacja zależna od serwera e-mail)
# #         elif user and check_password_hash(user.password_hash, password):
# #             session['user'] = user.email
# #             return redirect(url_for('consent'))
# #         else:
# #             flash('Incorrect email or password.', 'error')
# #
# #     return render_template('login.html')
#
# @app.route('/database')
# def database_shows_participants():
#     # Pobieranie wszystkich uczestników z bazy danych
#     participants = Participants.query.all()
#     # Przekazanie danych do szablonu 'participants.html'
#     #return render_template('dddatabase.html', database=database)
#     html = render_template("dddatabase.html", participants=participants)
#     print(html)
#     return html
#
#
# @app.route('/consent', methods=['GET', 'POST'])
# def consent():
#     if request.method == 'POST':
#         if 'agree' in request.form:
#             return redirect(url_for('database_shows_participants'))
#         else:
#             # Usuń użytkownika z bazy danych
#             user = Participants.query.filter_by(email=session['user']).first()
#             if user:
#                 db.session.delete(user)
#                 db.session.commit()
#             session.pop('user', None)
#             return redirect(url_for('index'))
#     return render_template('consent.html')
#
#
# @app.route('/coordination', methods=['GET', 'POST'])
# def coordination():
#     if 'coordinator' in session:
#         if request.method == 'POST':
#             fortress = request.form['fortress']
#             first_name = request.form['first_name']
#             last_name = request.form['last_name']
#             email = request.form['email']
#             phone_number = request.form['phone_number']
#             additional_info = request.form['additional_info']
#
#             auto_password = generate_password()  # Automatyczne hasło
#
#             # Tworzenie nowego uczestnika
#             new_participant_coord = Participants(
#                 fortress=fortress,
#                 first_name=first_name,
#                 last_name=last_name,
#                 email=email,
#                 phone_number=phone_number,
#                 additional_info=additional_info,
#                 password_hash=generate_password_hash(auto_password)
#             )
#             db.session.add(new_participant_coord)
#             db.session.commit()
#
#             # Wysłanie powiadomień e-mail
#             send_registration_email(email, auto_password)
#
#             flash("Data submitted successfully. A confirmation email has been sent.", 'success')
#         return render_template('coordination.html')
#     return redirect(url_for('index'))
#
# # @app.route('/registration', methods=['GET', 'POST']) = overwelming - is to remove
# # def registration():
# #     if request.method == 'POST':
# #         fortress = request.form.get('fortress')
# #         first_name = request.form.get('first_name')
# #         last_name = request.form.get('last_name')
# #         email = request.form.get('email')
# #         phone_number = request.form.get('phone_number')
# #         additional_info = request.form.get('additional_info')
# #         password_hash = request.form.get('password')
# #
# #
# #         if Participants.query.filter_by(email=email).first():
# #             flash("This email is already registered. Please use a different email.", 'error')
# #             return redirect(url_for('registration'))
# #
# #         # Generowanie automatycznego hasła
# #         auto_password = generate_password()  # Można zastąpić bardziej złożonym generatorem haseł
# #
# #         # Tworzenie nowego uczestnika
# #         new_participant_regist = Participants(
# #             fortress=fortress,
# #             first_name=first_name,
# #             last_name=last_name,
# #             email=email,
# #             phone_number=phone_number,
# #             additional_info=additional_info,
# #             password_hash=generate_password_hash(auto_password)
# #         )
# #         db.session.add(new_participant_regist)
# #         db.session.commit()
# #
# #         # Wysłanie powiadomień e-mail
# #         send_registration_email(email, auto_password)
# #
# #         flash("Registration successful! A confirmation email has been sent.", 'success')
# #         return redirect(url_for('index'))
# #     return render_template('registration.html')
#
# @app.route('/send_message/<email>', methods=['POST'])
# def send_message(email):
#     if request.method == 'POST':
#         subject = request.form['subject']
#         message_body = request.form['message']
#         msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[email])
#         msg.body = message_body
#         mail.send(msg)
#         flash("Message sent successfully.")
#         return redirect(url_for('coordination'))
#
# @app.route('/send_message_all', methods=['POST'])
# def send_message_all():
#     if request.method == 'POST':
#         subject = request.form['subject']
#         message_body = request.form['message']
#         participants = Participants.query.all()
#         recipients = [p.email for p in participants]
#         msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=recipients)
#         msg.body = message_body
#         mail.send(msg)
#         flash("Message sent to all participants successfully.")
#         return redirect(url_for('coordination'))
#
# # @app.route('/', methods=['GET', 'POST'])
# # def translate_page():
# #     translated_text = None
# #
# #     if request.method == 'POST':
# #         # Pobranie tekstu i języka docelowego z formularza
# #         text_to_translate = request.form.get('about')
# #         target_language = request.form.get('language')
# #
# #         if text_to_translate and target_language:
# #             try:
# #                 # Tłumaczenie tekstu
# #                 translated_text = ts.translate(text_to_translate, dest=target_language).text
# #             except Exception as e:
# #                 flash(f"Error during translation: {str(e)}", "error")
# #         else:
# #             flash("Please provide text and select a language.", "warning")
# #
# #     return render_template('translate.html', translated_text=translated_text)
#
#
# @app.route('/reset_password_request', methods=['GET', 'POST'])
# def reset_password_request():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         user = Participants.query.filter_by(email=email).first()
#
#         if user:
#             # Generowanie unikalnego tokenu do resetowania hasła
#             s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
#             token = s.dumps(email, salt='password-reset-salt')
#
#             # Tworzenie linku do zresetowania hasła
#             reset_url = url_for('reset_password', token=token, _external=True)
#
#             # Wysyłanie e-maila
#             msg = Message(
#                 "Password Reset Request",
#                 sender=app.config['MAIL_USERNAME'],
#                 recipients=[email]
#             )
#             msg.body = f"Click the link to reset your password: {reset_url}"
#             mail.send(msg)
#
#             flash("An email has been sent with instructions to reset your password.", 'info')
#         else:
#             flash("No account found with that email address.", 'error')
#
#     return render_template('reset_password_request.html')
#
# @app.route('/reset_password/<token>', methods=['GET', 'POST'])
# def reset_password(token):
#     s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
#     try:
#         # Walidacja tokenu (ważność: 3600 sekund = 1 godzina)
#         email = s.loads(token, salt='password-reset-salt', max_age=3600)
#     except Exception:
#         flash("The reset link is invalid or has expired.", 'error')
#         return redirect(url_for('reset_password_request'))
#
#     if request.method == 'POST':
#         new_password = request.form.get('password')
#         confirm_password = request.form.get('confirm_password')
#
#         if new_password == confirm_password:
#             user = Participants.query.filter_by(email=email).first()
#             if user:
#                 user.password_hash = generate_password_hash(new_password)
#                 db.session.commit()
#                 flash("Your password has been reset successfully.", 'success')
#                 return redirect(url_for('login'))
#         else:
#             flash("Passwords do not match.", 'error')
#
#     return render_template('reset_password.html')
#
# def send_registration_email(recipient_email, password):
#     try:
#         subject = "Registration on the Biehler Forts website was carried out"
#         body = (
#             f"You are registered on the ‘Biehler Forts’ website.\n\n"
#             f"Link to the page: https://www.biehlerforts.com\n"
#             f"The password was assigned automatically: {password}\n\n"
#             f"Please go to the website and change your password to the original one.\n"
#         )
#
#         # Wysłanie wiadomości do uczestnika
#         msg_to_participant = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient_email])
#         msg_to_participant.body = body
#         mail.send(msg_to_participant)
#
#         # Wysłanie wiadomości do administratora
#         msg_to_admin = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=coordinator_email)
#         msg_to_admin.body = f"The participant {recipient_email} has carried out the registration."
#         mail.send(msg_to_admin)
#
#     except Exception as e:
#         print(f"Error while sending an e-mail: {e}")
#
# def generate_password(length=12):
#     alphabet = string.ascii_letters + string.digits + "!@#$%^&*()"
#     return ''.join(secrets.choice(alphabet) for _ in range(length))
#
# @app.route('/')
# def send_email():
#   msg = Message(
#     'Hello',
#     recipients=['biehler.forts@gmail.com'],
#     body='This is a test email sent from Flask-Mail!'
#   )
#   mail.send(msg)
#   print('Email sent succesfully!')
#   return 'Email sent succesfully!'
#
# # @app.errorhandler(404)
# # def not_found_error(error):
# #     return render_template('404.html'), 404
# #
# # @app.errorhandler(500)
# # def internal_error(error):
# #     db.session.rollback()
# #     return render_template('500.html'), 500
#
#
# # #SCRIPT pozwala usuwać zawartosc bazy danych!
# # with app.app_context():
# #     # Usuń wszystkich uczestników
# #     db.session.query(Participants).delete()
# #     db.session.commit()
#
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from models import db, User, Participants
from auth import auth as auth_blueprint
from main import main as main_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'your-secret-key'

# Inicjalizacja bazy danych
db.init_app(app)
migrate = Migrate(app, db)

# Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Rejestracja blueprintów
app.register_blueprint(auth)
app.register_blueprint(main)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Tworzenie tabel w bazie danych
    app.run(debug=True)