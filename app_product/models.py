from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "categories"


class Product(models.Model):
    product_title = models.CharField(max_length=255, unique=True)
    product_description = models.CharField(max_length=255)
    product_amount = models.IntegerField()
    product_price = models.FloatField()
    product_images = models.ImageField()
    product_active = models.BooleanField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_title

    class Meta:
        db_table = 'products'
        verbose_name_plural = 'products'


class Shop(models.Model):
    shop_title = models.CharField(max_length=255, unique=True)
    shop_description = models.CharField(max_length=255)

    def __str__(self):
        return self.shop_title

    class Meta:
        db_table = "shop"
        verbose_name_plural = "shops"
