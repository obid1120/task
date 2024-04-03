from django.urls import path

from .views import login_view, register_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('', login_view, name='home'),
]