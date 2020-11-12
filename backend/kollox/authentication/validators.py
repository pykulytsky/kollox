from django.core.exceptions import ValidationError

def validate_age(age):
    if isinstance(age, str):
        if age < 1:
            raise ValidationError(f"Your age is to low({age}), must be at least 1.")
        if age > 120:
            raise ValidationError(f"Your age is to high({age}), must be max 120.")