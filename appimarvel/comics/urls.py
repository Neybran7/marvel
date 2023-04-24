from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


urlpatterns=[
    path('',views.inicio, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/',LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='social/logout.html'),name='logout'),    
]