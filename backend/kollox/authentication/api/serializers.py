from authentication.models import User, UserManager
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import login


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)


    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token', )

    
    def create(self, validated_data) -> User:
        return User.objects.create_user(**validated_data)

    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    username = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)


    def validate(self, validation_data) -> dict:
        email = validation_data.get('email', None)
        password = validation_data.get('password', None)

        if email is None:
            raise serializers.ValidationError("Для входу потрібна пошта.")

        if password is None:
            serializers.ValidationError('Для входу потрібен пароль.')
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError("Такого користувача не знайдено.")

        if not user.is_active:
            raise serializers.ValidationError("Користувач не активний.")

        return {
            'token' : user.token
        }

        
