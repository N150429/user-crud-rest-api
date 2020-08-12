from django.db import models
from phone_field import PhoneField
# Create your models here.
class Users(models.Model):
	first_name = models.CharField(max_length=200,blank=True)
	last_name = models.CharField(max_length=200,blank=True)
	phone = PhoneField(blank=True, help_text='Contact phone number')
	email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
	company = models.CharField(max_length=200,blank=True)
	company_location = models.CharField(max_length=200,blank=True)
	address = models.TextField(max_length=250,blank=True)
