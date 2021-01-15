from .models import User
from typing import Optional, Tuple
from django.core.mail import send_mail

from django.conf import settings


class UserCreator:
    def __init__(self,
                 username: str,
                 email: str,
                 password: str,
                 first_name: Optional[str] = '',
                 last_name: Optional[str] = ''
                 ):
        self.username = username
        self.email = email
        self.password = password

        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()

    @property
    def get_full_name(self) -> str:
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.username

    def create(self) -> Tuple[User, bool]:
        _user = User.objects.update_or_create(username=self.username,
                                              email=self.email,
                                              password=self.password,
                                              first_name=self.first_name,
                                              last_name=self.last_name)

        if settings.DEBUG and _user[0].email_verified is False:
            self.send_verification_mail()

        return _user

    @property
    def user(self) -> User:
        return self.create()[0]

    def send_verification_mail(self) -> None:

        send_mail(
            'Please, verify your account',
            f'Please, verify your account by using this verification code: {self.user.email_verification_code}',

            settings.EMAIL_HOST_USER,
            [self.email, ],
            fail_silently=False
        )
