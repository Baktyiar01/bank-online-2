from django.urls import path

from . import views
from .views import UserRegistrationView, LogoutView, UserLoginView

app_name = 'bankapps'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
]