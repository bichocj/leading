from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('webhook', views.webhook, name='webhook'),
    path('panel/', views.dashboard, name='dashboard'),
]