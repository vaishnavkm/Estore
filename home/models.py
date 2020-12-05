from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pics')
    detail=models.CharField(max_length=500)
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    
   

class new_models(models.Model):
    item=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    description=models.CharField(max_length=500)
    money=models.IntegerField()
    discount=models.BooleanField(default=False)


class register_id(models.Model):
    username=models.TextField(max_length=10)
    first_name=models.TextField(max_length=10)
    last_name=models.TextField(max_length=10)
    email=models.EmailField()
    password1=models.CharField(max_length=10)
    password2=models.CharField(max_length=10)
    number=models.IntegerField()



  






    
