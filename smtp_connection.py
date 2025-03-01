import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = 'biehler.forts@gmail.com'
msg['To'] = 'biehler.forts@gmail.com'
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp-relay.brevo.com', 587)   #'smtp.sendgrid.net'
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('80abd6001@smtp-brevo.com', 'Y4XPKv2EDmc3nN1Z')

mailserver.sendmail('michal.mietus@gmail.com','biehler.forts@gmail.com',msg.as_string())

mailserver.quit()

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
# mailserver = smtplib.SMTP('smtp.sendgrid.net',587)   #'smtp.sendgrid.net'
# # identify ourselves to smtp gmail client
# mailserver.ehlo()
# # secure our email with tls encryption
# mailserver.starttls()
# # re-identify ourselves as an encrypted connection
# mailserver.ehlo()
# mailserver.login('apikey', 'SENDGRID_API_KEY')
#
# mailserver.sendmail('biehler.forts@gmail.com','biehler.forts@gmail.com',msg.as_string())
#
# mailserver.quit()


# import smtplib
# from flask import Flask
# from flask_mail import Mail, Message
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# app = Flask(__name__)
#
# # Configure Flask-Mail
# app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_USERNAME'] = 'apikey'
# app.config['MAIL_PASSWORD'] = os.getenv('SENDGRID_API_KEY')
# app.config['MAIL_DEFAULT_SENDER'] = 'biehler.forts@gmail.com'
#
# mail = Mail(app)
#
# # @app.route('/send_email')
# # def send_email():
# #     try:
# #         # Enable debugging for SMTP
# #         mail.debug = True
# #
# #         # Create the message
# #         msg = Message(
# #             subject="Hello from SendGrid",
# #             sender=app.config['MAIL_DEFAULT_SENDER'],
# #             recipients=["michail.lysenk@gmail.com"],
# #             body="This is a test email sent using SendGrid SMTP!"
# #         )
# #         mail.send(msg)
# #         return "Email sent successfully!"
# #     except smtplib.SMTPException as e:
# #         return f"SMTP error: {e}"
# #     except Exception as e:
# #         return f"Failed to send email: {str(e)}"
#
# @app.route('/send_email')
# def send_email():
#     try:
#         msg = Message(
#             subject="Hello from SendGrid",
#             sender=app.config['MAIL_DEFAULT_SENDER'],
#             recipients=["michail.lysenk@gmail.com"],  # Zmień na swój email testowy
#             body="This is a test email sent using SendGrid SMTP!"
#         )
#         mail.send(msg)
#         return "Email sent successfully!"
#     except Exception as e:
#         print(f"Failed to send email: {e}")
#         return f"Failed to send email: {e}", 500
#
# if __name__ == '__main__':
#     app.run(debug=True)
#

