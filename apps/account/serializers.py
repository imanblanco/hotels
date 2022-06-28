from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('nickname', 'email', 'password', 'password_confirm')

    def validate_nickname(self, nickname):
        if User.objects.filter(nickname=nickname).exists():
            return serializers.ValidationError('This nickname is already token. Please choose another one')
        return nickname

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email is already exists')
        return email

    def validate(self, attrs: dict):
        print(attrs)
        password1 = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if not any(i for i in password1 if i.isdigit()):
            raise serializers.ValidationError('Password must contain at least on digit')
        if password1 != password_confirm:
            raise serializers.ValidationError('Password do not match')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.create_activation_code()
        send_activation_sms.delay(user.phone, user.activation_code)
        return user

