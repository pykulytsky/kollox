from django.core.mail import send_mail
from django.conf import settings

def send_share_email(to_email):
    send_mail(
        'Some user just share todo list',
        'Some one share todo list to you, please check it!',
        settings.EMAIL_HOST_USER,
        [to_email, ],
        fail_silently=False
    )