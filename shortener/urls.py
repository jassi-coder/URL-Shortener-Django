from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:code>/', views.redirect_to_original, name='redirect'),
]
