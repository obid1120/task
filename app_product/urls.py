from django.urls import path

from .views import ProductListView, AddProductView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('add/', AddProductView.as_view(), name='add'),
]