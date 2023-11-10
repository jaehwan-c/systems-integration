from django.db import models

# Create your models here.

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE, verbose_name='Customer')
    product_id = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.IntegerField(verbose_name='Order_quantity')
    
    class Meta():
        db_table = 'order'
        verbose_name = 'order'