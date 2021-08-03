from django.db import models

from customers.models import customers
from profiles.models import Profile
from products.models import Product
# Create your models here.
class Position(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantitiy=models.PositiveIntegerField()
    price=models.FloatField(blank=True)
    created=models.DateTimeField(blank=True)

    def save(self,*args ,**kwargs):
        self.price=self.product.price*self.quantity
        return super().save(*args,**kwargs)
    



    def __str__(self):
        return f"id: {self.id}, product: {self.product.name}, quantity: {self.quantity}"
class Sales(models.Model):
    tran_id=models.CharField(max_length=12,blank=True)
    positions=models.ManyToManyField(Position)
    total_price=models.FloatField(blank=True)
    customer=models.ForeignKey(customers,on_delete=models.CASCADE)
    salesman=models.ForeignKey(Profile,on_delete=models.CASCADE)
    created=models.DateTimeField(blank=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"sales for the amount ${self.total_price}"

    def save(self, *args ,**kwargs):
        if self.tran_id=="":
            self.tran_id==''
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args,**kwargs)
    def get_position(self):
       return self.position.all()
    
class CSV(models.Model):
    file_name=models.FileField(upload_to="csvs")
    activated=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.file_name)
    
