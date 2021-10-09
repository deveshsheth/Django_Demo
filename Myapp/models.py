from django.db import models

# Create your models here.
class bookmodel(models.Model):
    book_name = models.CharField(max_length=30)
    author_name = models.CharField(max_length=30)
    quantity = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    book_categories = models.CharField(max_length=30)

class signupmodel(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phoneno = models.CharField(max_length=30)
