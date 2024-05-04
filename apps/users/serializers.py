from rest_framework import serializers
from rest_framework.validators import UniqueValidator, ValidationError

from .models import User


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='User with such email already exists'
            )
        ]
    )
    password = serializers.CharField()
    password_confirmation = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def validate_password_confirmation(self, value):
        if value != self.initial_data.get('password'):
            raise ValidationError('Passwords must be similar')

    def create(self, validated_data):
        user = User(
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user

