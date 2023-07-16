from django.core.mail import send_mail

from config import settings


def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        recipient_list
    )