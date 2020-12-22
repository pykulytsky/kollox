from django.core.mail import send_mail
from django.template.loader import render_to_string
import uuid
from .models import User
import logging

logger = logging.getLogger('main')

def send_verification_email(verification_code: uuid) -> None:
    try:
        user = User.objects.get(email_verification_code=verification_code)
    except User.DoesNotExist:
        logger.warning(f"Error, while verification email\n[user]: {user}\nCant find user.")

    if not user.email_verified:
        send_mail(
            subject='Verify Your Account',
            message=
        )