from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import Participants
from flask import Blueprint
from app.auth import auth_bp
#from app.main import main_bp
#from dotenv import load_dotenv
from app.db import db
#import os

auth_bp = Blueprint('auth', __name__, template_folder='templates')

# coordinator_email = os.getenv('COORDINATOR_EMAIL')
# coordinator_password = os.getenv('COORDINATOR_PASSWORD')

@auth_bp.route('/signup')
def signup():
    return render_template('auth/signup.html')

@auth_bp.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    fortress = request.form.get('fortress')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = Participants.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = Participants(fortress=fortress, email=email, first_name=first_name, last_name=last_name, password_hash=generate_password_hash(password))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')

@auth_bp.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Participants.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password_hash, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    login_user(user, remember=False, duration=None, force=False, fresh=True)
    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('auth.consent'))

@auth_bp.route('/consent', methods=['GET', 'POST'])
@login_required
def consent():
    if request.method == 'POST':
        if 'agree' in request.form:
            return redirect(url_for('auth.database'))
        else:
            # Usuń użytkownika z bazy danych
            user = Participants.query.filter_by(email=session['user']).first()
            if user:
                db.session.delete(user)
                db.session.commit()
            session.pop('user', None)
            return redirect(url_for('main.index'))
    return render_template('auth/consent.html')


@auth_bp.route('/database')
@login_required
def database():
    participants = Participants.query.all()  # Funkcja pobierająca uczestników z bazy
    return render_template('main/database.html', participants=participants, user=current_user)

@auth_bp.route('/add_user_as_coordinator', methods=['POST'])
@login_required
def add_user_as_coordinator():
    if not current_user.coordinator:
        return "Access forbidden", 403  # Forbidden

    fortress = request.form.get('fortress')
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    # Dodaj użytkownika do bazy
    new_user = Participants(fortress=fortress, email=email, first_name=first_name, last_name=last_name, coordinator=False)
    db.session.add(new_user)
    db.session.commit()

    return render_template('main/database.html', participants=Participants, user=current_user)



@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))



#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
#
#             # return redirect(url_for('auth.coordination'))
#
#         # Logowanie uczestnika
#         participant = Participants.query.filter_by(email=email).first()
#         if not participant or not participant.check_password_hash(user.password, password):
#             flash('Invalid email or password. Please try again.')
#             return redirect(url_for('auth.login'))
#         # if not user or not check_password_hash(user.password, password):
#
#         login_user(participant)
#         return redirect(url_for('auth.profile'))
#
#     return render_template('auth/login.html')
#
# @auth_bp.route('/coordination', methods=['GET', 'POST'])
# @login_required
# def coordination():
#     # Sprawdzenie, czy użytkownik jest koordynatorem
#     if not hasattr(current_user, 'coordinator') or not current_user.coordinator:
#         flash("You do not have permission to access this page.")
#         return redirect(url_for('auth.login'))
#
#     if request.method == 'POST':
#         fortress = request.form['fortress']
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         email = request.form['email']
#         phone_number = request.form['phone_number']
#         additional_info = request.form['additional_info']
#
#         # Sprawdzenie, czy uczestnik o podanym e-mailu już istnieje
#         if Participants.query.filter_by(email=email).first():
#             flash("Participant with this email already exists.")
#             return redirect(url_for('auth.coordination'))
#
#         # Dodanie nowego uczestnika do bazy danych
#         new_participant = Participants(
#             fortress=fortress,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             phone_number=phone_number,
#             additional_info=additional_info,
#             coordinator = False
#         )
#         db.session.add(new_participant)
#         db.session.commit()
#         flash("New participant added successfully.")
#         return redirect(url_for('auth.coordination'))
#
#     # Pobranie listy uczestników
#     participants = Participants.query.all()
#     return render_template('auth/coordination.html', participants=participants)
#
#
#
#         # Wysłanie powiadomień e-mail
#         # email = new_participant_coord.email
#         # send_confirmation_email(email)
#         #
#         # flash("Data submitted successfully. A confirmation email has been sent.", 'success')
#         # return render_template('auth/register_success.html', message="E-mail z linkiem do ustawienia hasła został wysłany.")
#
#
#
#
# @auth_bp.route('/consent', methods=['GET', 'POST'])
# @login_required
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
#             return redirect(url_for('main.index'))
#     return render_template('consent.html')
#
# #@app.route('/database')
# # def database_shows_participants():
# #     # Pobieranie wszystkich uczestników z bazy danych
# #     participants = Participants.query.all()
# #     # Przekazanie danych do szablonu 'participants.html'
# #     #return render_template('dddatabase.html', database=database)
# #     html = render_template("dddatabase.html", participants=participants)
# #     print(html)
# #     return html
# #
# #
#
#
# @auth_bp.route('/confirm_email/<token>', methods=['GET'])
# def confirm_email(token):
#     try:
#         # Sprawdzenie tokena
#         email = confirm_token(token)  # Funkcja dekodująca token
#         participant = Participant.query.filter_by(email=email).first()
#
#         if participant:
#             return render_template('auth/set_password.html', participant=participant)  # Szablon do ustawienia hasła
#         else:
#             return redirect(url_for('auth.register'))  # Przekierowanie do rejestracji, jeśli uczestnik nie istnieje
#     except:
#         return "Link wygasł lub jest niepoprawny"
#
# @auth_bp.route('/register', methods=['GET', 'POST'])
# def register():
#     # Twoja logika rejestracji
#     return render_template('register.html')
#
