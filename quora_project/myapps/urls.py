from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.front_page, name='home'),
    path('post_question/', views.post_question, name='post_question'),
    path('view_question/<int:question_id>/', views.view_question, name='view_question'),
    path('post_answer/<int:question_id>/', views.post_answer, name='post_answer'),
    path('like_answer/<int:answer_id>/', views.like_answer, name='like_answer'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]

