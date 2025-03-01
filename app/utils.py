from flask_mail import Message, Mail
from flask import url_for, current_app
from itsdangerous import URLSafeTimedSerializer



def generate_reset_token(user, expires_sec=3600):
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return s.dumps(user.email, salt="reset-password")


def send_reset_email(user):
    token = generate_reset_token(user)
    reset_url = url_for('auth.reset_token', token=token, _external=True)

    msg = Message("Reset Your Password",
                  sender=current_app.config.get('MAIL_DEFAULT_SENDER', current_app.config['MAIL_USERNAME']),
                  recipients=[user.email])

    msg.body = f"""Hello {user.first_name},

You have been added as a participant. Please set your password by clicking the link below:

{reset_url}

If you did not request this, please ignore this email.
"""
    mail.send(msg)