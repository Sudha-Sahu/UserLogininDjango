# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .models import User
# from .serializer import UserSerializer


# class UserRegistrationView(APIView):
#     def post(self, request):
#         new_user = request.data
#         serializer = UserSerializer(data=new_user)
#         username = serializer.data.get('username')
#         password = serializer.data.get('password')
#         conf_password = serializer.data.get('conf_password')
#         if not conf_password == password:
#             return Response({'Message': 'password didnt match, register again', 'Code': 404})
#         user = User.objects.create_user(username=username, password=password)
#         user.save()
#         return Response({'Message': 'User added', 'Code': 200})
#

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer, RegisterSerializer, LoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics


# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        print(request.data)
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


# Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print(user)
        login(request, user)
        return Response({"message": "user logged in", "status": status.HTTP_200_OK})


class LogoutAPIView(APIView):
    def get(self, request):
        logout(request)
        return Response({'Message': 'You are Logged Out', "status": status.HTTP_200_OK})

