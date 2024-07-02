from django.db import models
import uuid
from django.contrib.auth.models import User

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=30,null=True,blank=True)
    phone_number = models.CharField(max_length=10,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    mail_id=models.TextField(null=True,blank=True)
    def __str__(self):
        return f'{self.name},{self.id}'
    
class Seller(models.Model):
    id=  models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=30,null=True,blank=True)
    company_name= models.CharField(max_length=30,null=True,blank=True)
    GST_NO=models.TextField(null=True,blank=True)
    phone_number = models.CharField(max_length=10,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    mail_id=models.TextField(null=True,blank=True)
    passport_size_photo=models.ImageField(upload_to="seller_field",null=True,blank=True)
    def __str__(self):
        return f'{self.name},{self.id}'
    
