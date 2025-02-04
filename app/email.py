# Konfiguracja e-maili
# Wysyłanie wiadomości
# Generowanie treści e-maili przy pomocy szablonów Jinja2


from flask_mail import Message
from flask import url_for
from flask import render_template
from app import mail  # Upewnij się, że mail jest odpowiednio zaimportowany

def send_email(to, subject, template, **kwargs):
    msg = Message(subject, recipients=[to], html=template, sender=app.config['MAIL_DEFAULT_SENDER'])
    msg.html = render_template(template, **kwargs)  # Zmienna szablon jest teraz renderowana
    mail.send(msg)

def send_confirmation_email(participant_email):
    token = generate_confirmation_token(participant_email)  # Funkcja generująca token (np. JWT)
    confirm_url = url_for('auth.confirm_email', token=token, _external=True)  # Zakładając, że masz blueprint auth
    send_email(participant_email,
               "Ustaw swoje hasło",
               'confirmation_email.html',  # Używamy szablonu Jinja2
               confirm_url=confirm_url)  # Przekazujemy URL do szablonu


@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']

    # Sprawdzenie, czy uczestnik już istnieje
    if Participant.query.filter_by(email=email).first():
        return render_template('auth/register_error.html', message="Uczestnik o podanym adresie e-mail już istnieje.")

    # Tworzenie nowego uczestnika
    new_participant = Participant(email=email)
    db.session.add(new_participant)
    db.session.commit()

    # Wysyłanie e-maila z linkiem do ustawienia hasła
    send_confirmation_email(email)

    return render_template('auth/register_success.html', message="E-mail z linkiem do ustawienia hasła został wysłany.")

 # <td><a href="{{ url_for('send_email', email=participant.email) }}">Send message</a> {{ participant.id }}</td>