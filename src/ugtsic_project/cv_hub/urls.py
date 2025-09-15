from django.urls import path
from django.contrib.auth import views as auth_views
from .views.auth import register_view, login_view 
from .views.home import HomePageView
from .views.cvform import CVCreateView

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('home/', HomePageView.as_view(), name='home_page'),
    path('home/create/', CVCreateView.as_view(), name='cv_create'),
]