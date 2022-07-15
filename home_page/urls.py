from django.urls import path
from django.contrib.auth import views as auth_views

from home_page import views

urlpatterns = [
    path('home/', views.HomePage.as_view()),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
