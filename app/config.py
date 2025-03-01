import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sekretny_klucz'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    MAIL_SERVER = 'smtp-relay.brevo.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = 'biehler.forts@gmail.com'
    SECURITY_PASSWORD_SALT = 'random_salt_string'

    #
    # import smtplib
    # from email.mime.multipart import MIMEMultipart
    # from email.mime.text import MIMEText
    #
    # msg = MIMEMultipart()
    # msg['From'] = 'biehler.forts@gmail.com'
    # msg['To'] = 'biehler.forts@gmail.com'
    # msg['Subject'] = 'simple email in python'
    # message = 'here is the email'
    # msg.attach(MIMEText(message))
    #
    # mailserver = smtplib.SMTP('smtp-relay.brevo.com', 587)  # 'smtp.sendgrid.net'
    # # identify ourselves to smtp gmail client
    # mailserver.ehlo()
    # # secure our email with tls encryption
    # mailserver.starttls()
    # # re-identify ourselves as an encrypted connection
    # mailserver.ehlo()
    # mailserver.login('80abd6001@smtp-brevo.com', 'Y4XPKv2EDmc3nN1Z')
    #
    # mailserver.sendmail('michal.mietus@gmail.com', 'biehler.forts@gmail.com', msg.as_string())
    #
    # mailserver.quit()