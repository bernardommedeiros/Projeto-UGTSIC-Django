from django.urls import path
from django.contrib.auth import views as auth_views
from .views.auth import register_view

urlpatterns = [
    path('register/', register_view, name='register'),
]
