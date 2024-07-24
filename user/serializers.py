from djoser.serializers import UserSerializer, UserCreateSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate 
from django.utils.translation import gettext as _

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['first_name', 'last_name', 'email', 'password']


class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

    @classmethod
    def get_token(cls, user):
        token = RefreshToken.for_user(user)
        return token

    def create(self, validated_data):
        user = validated_data['user']
        token = self.get_token(user)

        return {
            'refresh': str(token),
            'access': str(token.access_token),
        }
