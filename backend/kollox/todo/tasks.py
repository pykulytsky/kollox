from config.celery import app
from django.core.mail import send_mail
from django.template.loader import render_to_string
from typing import Any
from django.conf import settings
from .utils import send_share_email


@app.task
def send_verification_email(to_email: str) -> Any:
    send_mail(
        'Verify your account',
        'To verify your account, enter the code at the bottom of the input window, or just follow the link below',
        settings.EMAIL_HOST_USER,
        [to_email, ],
        fail_silently=False
    )
