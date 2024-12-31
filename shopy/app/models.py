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
    
#
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.TextField(max_length=300)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.product_name   
