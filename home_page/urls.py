from django.urls import path
from django.contrib.auth import views as auth_views

from home_page import views

urlpatterns = [
    path('home/', views.HomePage.as_view(), name='homepage'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path("register/", views.RegisterView.as_view(), name='register'),
    path("home/feedback-post", views.PostFeedback.as_view(), name="feedback_post"),
    path("get_feedbacks", views.ListFeedback.as_view(), name="feedback_list"),
    path("delete/feedback", views.DeleteFeedback.as_view(), name="delete_feedback"),
    path("show/feedback", views.ShowFeedback.as_view(), name="show_feedback"),
    path("get_users", views.ListUser.as_view(), name="user_list"),
    path("delete/user", views.DeleteUser.as_view(), name="delete_user"),
    path("check_feedbacks", views.CheckFeedback.as_view(), name="check_feedback_list"),

]
