from flask import Blueprint
from flask import current_app
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from flask_mail import Mail, Message
from werkzeug.security import check_password_hash, generate_password_hash
from app.auth.forms import FlaskForm

from app.db import db
from app.models import Participants


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

    return render_template('main/database.html', user=current_user)

@auth_bp.route("/send-email", methods=['POST'])
def send_message_to_all_participants():
    # Pobieramy wiadomość od użytkownika z formularza
    message_text = request.form.get("text")
    if not message_text:  # 👀 Jeśli użytkownik nic nie wpisał
        flash("Message cannot be empty!", "danger")  # 🚨 Pokaż komunikat
        return redirect(url_for('auth.send_message_to_all_participants', user=current_user))

    # List of recipients
    recipients = ["michail.lysenk@gmail.com"]

    # Creating the message
    msg = Message("Email to Multiple Recipients",
                  sender=current_app.config.get('MAIL_DEFAULT_SENDER', current_app.config['MAIL_USERNAME']),
                  #  Pobiera domyślnego nadawcę
                  recipients=recipients)
    msg.body = message_text

    # Sending the email
    with current_app.app_context():
        mail = Mail()
        mail.send(msg)

    flash("Email sent successfully!", "success")  #  Komunikat o sukcesie
    return redirect(url_for('main.database'))  #  Możesz zmienić na inną stronę


@auth_bp.route('/reset_password', methods=['GET', 'POST'])
def reset_password_request():
    if request.method == 'POST':
        email = request.form['email']
        user = Participants.query.filter_by(email=email).first()  # Znajdź użytkownika w bazie

        if user:
            token = user.generate_reset_token()  # Teraz token generuje się na obiekcie User
            reset_url = url_for('auth.reset_password', token=token, _external=True)

            msg = Message('Password Reset Request', sender='biehler.forts@gmail.com', recipients=[email])
            msg.body = f'Please click the link to reset your password: {reset_url}'

            mail = Mail()
            mail.send(msg)

            flash('A password reset link has been sent to your email.', 'info')
        else:
            flash('No account found with that email.', 'warning')

        return redirect(url_for('auth.login'))

    return render_template('auth/reset_password_request.html')


@auth_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    email = Participants.verify_token(token)  # ✅ Teraz verify_token jest wywoływane poprawnie!

    if not email:
        flash('The reset link is invalid or has expired.', 'danger')
        return redirect(url_for('auth.reset_password_request'))  # Poprawiony redirect

    if request.method == 'POST':
        new_password = request.form['password']
        user = Participants.query.filter_by(email=email).first()  # Pobieramy użytkownika po emailu

        if user:
            user.password_hash = generate_password_hash(new_password)
            db.session.commit()
            flash('Your password has been updated!', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('User not found.', 'danger')

    return render_template('auth/reset_password.html')

def send_reset_email(user):
    token = user.generate_reset_token()  # Uzyskiwanie tokenu
    reset_url = url_for('auth.reset_password', token=token, _external=True)  # Tworzenie URL z tokenem

    msg = Message("Reset your password",
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[user.email])
    msg.body = f"Click the link to reset your password: {reset_url}"

    mail = Mail(current_app)
    mail.send(msg)



#
# if __name__ == "__main__":
#     app.run(debug=True)



# @auth_bp.route("/send-email", methods=["GET", "POST"])
# @login_required
# def send_message_to_all_participants():
#     if request.method == "POST":
#         # Pobranie treści wiadomości z formularza
#         message_body = request.form.get("text")
#
#         # Pobranie wszystkich uczestników z bazy danych
#         participants = Participants.query.all()
#
#         # Tworzenie listy adresów e-mail
#         recipients = [p.email for p in participants]
#
#         if not recipients:
#             return "No participants to send emails to!", 400  # Jeśli brak uczestników
#
#         # Tworzenie wiadomości
#         msg = Message("Message to All Participants",
#                       sender="MAIL_USERNAME",
#                       recipients=recipients)
#         msg.body = message_body
#
#         # Wysłanie e-maila
#         mail.send(msg)
#
#         return "Email sent to all participants!"
#
#     return render_template("main/database.html")  # GET - renderowanie strony


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
