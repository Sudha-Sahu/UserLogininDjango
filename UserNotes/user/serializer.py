from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


# Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username"]


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
                'first_name': {'required': True},
                'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
                                username=validated_data['username'],
                                email=validated_data['email'],
                                first_name=validated_data['first_name'],
                                last_name=validated_data['last_name']
                              )
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        required_fields = fields

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                data['user'] = user
            data['user'] = user
        return data


class ResetPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'password',
            'confirm_password'
        ]








# def create(self, validated_data):
#     user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
#     # At this point, user is a User object that has already been
#     # saved to the database. You can continue to change its
#     # attributes if you want to change other fields.
#
#     user.first_name = validated_data['first_name']
#     user.last_name = validated_data['last_name']
#     user.save()
#     return user