from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext as _
from rest_framework import exceptions, serializers
from . import models


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value

    def validate(self, validated_data):
        new_password = validated_data['new_password']
        new_password2 = validated_data['new_password2']
        if new_password != new_password2:
            raise serializers.ValidationError('Las contraseñas no coinciden.')

        return validated_data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ('phone',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'profile', 'token')
        read_only_fields = ('token',)
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def get_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        # Validate email is not already in use.
        username = validated_data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            profile = validated_data.pop('profile')
            user = User.objects.create(**validated_data)
            user.set_password(validated_data['password'])
            user.save()

            user.profile.__dict__.update(profile)
            user.profile.save()

        return user
