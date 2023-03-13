from flask_mail import Message, Mail
from flask import render_template

def send_confirmation_email(abiola@urgency2021.com, meeting_details):
    # Initialize Flask-Mail extension
    mail = Mail()

    # Set up email message
    msg = Message(subject="Meeting Confirmation",
                  sender=("Abiola", "abiola@urgency201.com"),
                  recipients=['user_email'])

    # Render email body from template with meeting details
    body = render_template("confirmation_email.html"), ("zoom.calls='meeting_details")

    # Add body to email message
    msg.body = 'talk to the best in the cloud technogy business'

    # Send email
    mail.send(msg)
