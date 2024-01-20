from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    # def get_absolute_url(self):
    #     return reverse('store:category_list', args=[self.slug])
    
    def __str__(self):
        return self.name

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.brand
    
    class Meta():
        verbose_name = 'brand'

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='Category')
    slug = models.SlugField(max_length=255)
    name = models.CharField(max_length=128, verbose_name="ProductName", unique=True)
    brand_id = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='Brand')
    quantity = models.IntegerField(verbose_name='Quantity')
    price = models.IntegerField(verbose_name="ProductPrice")
    # Location -- from 1 to 10 for further processing
    LOCATION_CHOICES = [(x, x) for x in range(1, 11)]
    location = models.PositiveIntegerField(default=1, choices=LOCATION_CHOICES, verbose_name='Location')
    # Upload Images
    image = models.ImageField(upload_to='images/')
    #
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.name

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=64, verbose_name='name')
    email = models.EmailField(verbose_name="email")
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    address = models.CharField(max_length=512, verbose_name='address')
    
    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'customer'
        verbose_name = 'customer'