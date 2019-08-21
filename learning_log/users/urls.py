"""为应用程序users定义URL模式"""
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from . import views
urlpatterns=[
    #登录页面
    path('login/',LoginView.as_view(template_name='users/login.html'), name='login'),
    #注销
    path('logout/',LogoutView.as_view(next_page='/'),name='logout'),
    #
    path('register/',views.register, name='register'),
    ]
app_name='users'
