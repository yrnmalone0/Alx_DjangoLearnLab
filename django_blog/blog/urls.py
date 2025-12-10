from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path("login/", views.home, name="login"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]