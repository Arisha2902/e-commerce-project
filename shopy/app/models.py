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
    
class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/images')

    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    Order_id = models.AutoField(primary_key=True)
    items_json = models.TextField()
    name = models.CharField(max_length=90)
    email = models.EmailField(max_length=111)
    amount = models.IntegerField(default=0)
    address1 = models.CharField(max_length=111)
    address2 = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    oid = models.CharField(max_length=111 ,blank=True)
    amountpaid = models.CharField(max_length=500, blank=True, null=True)
    paymentstatus = models.CharField(max_length=500, blank=True)
    phone = models.CharField(max_length=111)

    def __str__(self):
        return self.name
    
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.TextField()
    delivered=models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."