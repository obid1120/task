from django.urls import path

from .views import register

urlpatterns = [
    # path('', )
    path('', register, name='register'),
]