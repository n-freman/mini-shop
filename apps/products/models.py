from django.db import models

from categories.models import Category


class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='products')

    class Meta:
        db_table = 'product_images'


class ProductColor(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='colors'
    )
    color = models.CharField(max_length=16)

    class Meta:
        db_table = 'product_color'


class ProductSize(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='sizes'
    )
    size = models.CharField(max_length=16)

    class Meta:
        db_table = 'product_size'

