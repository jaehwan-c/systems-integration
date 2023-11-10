from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=128, unique=True, verbose_name='Category')
    
    def __str__(self):
        return self.category
    
    class Meta():
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=128, unique=True, verbose_name='Brand')

    def __str__(self):
        return self.brand
    
    class Meta():
        verbose_name = 'brand'

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category')
    name = models.CharField(max_length=128, verbose_name="ProductName", unique=True)
    brand_id = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name='Brand')
    quantity = models.IntegerField(verbose_name='Quantity')
    price = models.IntegerField(verbose_name="ProductPrice")

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = 'product'