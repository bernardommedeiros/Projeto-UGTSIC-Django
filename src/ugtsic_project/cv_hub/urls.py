from django.urls import path
from django.contrib.auth import views as auth_views
from .views.auth import register_view, login_view 
from .views.home import HomePageView

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('home/', HomePageView.as_view(), name='home_page'),
]