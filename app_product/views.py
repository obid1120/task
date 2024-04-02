from django.views.generic import ListView, CreateView

from .models import Shop, Product


# Create your views here.
class AddProductView(CreateView):
    template_name = 'product/product_add.html'
    model = Product
    success_url = 'home'
    fields = '__all__'


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Shop
