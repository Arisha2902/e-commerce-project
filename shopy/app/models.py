from django.db import models



# Create your models here.
class Contact(models.Model):
    Contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    email = models.EmailField(max_length=100)
    phonenumber = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    Product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/images')

    def __str__(self):
        return self.product_name
