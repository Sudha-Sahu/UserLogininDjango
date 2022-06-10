# from django.urls import path
# from . import views
#
# urlpatterns = [
#
#     #path('api/hello', views.SimpleApI.as_view())
#     path('registration', views.UserRegistrationView.as_view())
# ]

from django.urls import path
from .views import UserDetailAPI, RegisterUserAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
  path("get-details", UserDetailAPI.as_view()),
  path('register', RegisterUserAPIView.as_view()),
  path('login', LoginAPIView.as_view()),
  path('logout', LogoutAPIView.as_view()),
]
