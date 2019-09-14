"""
Definition of urls for learning_log.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', include('learning_logs.urls',namespace='learning_logs')),
    path('admin/', admin.site.urls),
    path('users/',include('users.urls',namespace='users')),
    
]
