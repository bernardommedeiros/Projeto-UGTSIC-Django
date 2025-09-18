from django.urls import path
from django.contrib.auth import views as auth_views
from .views.auth import register_view, login_view, logout_view
from .views.home import HomePageView
from .views.cvform import CVCreateView, CVUpdateView
from .views.receipt import ReceiptGenerateView
from .views.mail import send_email

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

    path('home/', HomePageView.as_view(), name='home_page'),
    path('home/create/', CVCreateView.as_view(), name='cv_create'),
    path('home/<int:cv_id>/', ReceiptGenerateView.as_view(), name='receipt'),
    path('home/update/', CVUpdateView.as_view(), name='cv_update'),
     path('send_email/', send_email, name='enviar_email'),
]