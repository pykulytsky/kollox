from django.db import models
from django.conf import settings
from django.core import validators

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

import jwt
from jwt.exceptions import *
import uuid

from datetime import datetime
from datetime import timedelta

from authentication import validators as custom_validators
# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("User does not have an username")
        if not email:
            raise ValueError("User does not have an email")
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    
    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',  False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password=password, **extra_fields)


    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have extra field 'is_staff'=True")

        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have extra field 'is_superuser'=True")

        return self._create_user(username, email, password, **extra_fields)

    
class User(AbstractBaseUser, PermissionsMixin):
    """Custom User Model for JWT Authentication backend with permissions"""
    username = models.CharField(max_length=255, db_index=True, unique=True)
    email = models.EmailField(validators=[validators.validate_email], unique=True, blank=False)

    first_name = models.CharField(max_length=255, blank=True,verbose_name= "First Name")
    last_name = models.CharField(max_length=255, blank=True, verbose_name="Last Name")
    age = models.IntegerField(validators=[custom_validators.validate_age, ], verbose_name='Age', blank=True, null = True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    email_verified = models.BooleanField(default=False)
    email_verification_code = models.UUIDField(max_length=32, default=uuid.uuid4, editable=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', )

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        super().save(*args, **kwargs)    


    def __str__(self):
        return f'<User: {self.username}>'

    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    
    def get_short_name(self):
        return self.first_name

    
    @property
    def token(self, algorithm='HS256'):
        self._generate_jwt_token()

    
    def _generate_jwt_token(self, algorithm):
        dt = datetime.now() + timedelta(days=60)

        try:
            token = jwt.encode({
                'id': self.pk,
                'exp': dt.timestamp()
            },
            settings.SECRET_KEY,
            algorithm=algorithm)
        except (InvalidTokenError, DecodeError, InvalidAlgorithmError,
                InvalidAudienceError, ExpiredSignatureError, ImmatureSignatureError,
                InvalidIssuedAtError, InvalidIssuerError, ExpiredSignature,
                InvalidAudience, InvalidIssuer, MissingRequiredClaimError,
                InvalidSignatureError,
                PyJWTError):
                raise ValueError("Error occured while generating jwt token")

        return token.decode('utf-8')