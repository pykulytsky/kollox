from rest_framework import serializers
from authentication.models import User
from rest_framework.authentication import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'username',
                  'password',
                  'token',)

    def create(self, validated_data) -> User:
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    username = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    pk = serializers.IntegerField(read_only=True)

    def validate(self, validation_data) -> dict:
        email = validation_data.get('email', None)
        password = validation_data.get('password', None)

        if email is None:
            raise serializers.ValidationError("Для вєоду потрібна пошта.")

        if password is None:
            serializers.ValidationError('Для входу потрібен пароль.')
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError("Такого користувача не знайдено.")

        if not user.is_active:
            raise serializers.ValidationError("Користувач не активний.")

        return {
            'token': user.token,
            'pk': user.pk
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'first_name', 'last_name',)


class UserDetailSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'age',
                  "is_superuser",
                  'email_verified',
                  'avatar',
                  'avatar_url')

    def get_avatar(self, user):
        request = self.context.get('request')
        avatar = user.avatar.url
        return request.build_absolute_uri(avatar)
