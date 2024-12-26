from django.contrib import admin
from app.models import Contact,Product,Order,OrderUpdate

admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderUpdate)

# Register your models here.
