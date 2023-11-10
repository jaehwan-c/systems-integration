from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

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