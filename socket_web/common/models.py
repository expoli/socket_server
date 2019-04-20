from django.db import models

# Create your models here.

class Customer(models.Model):
    # 
    string1 = models.TextField(max_length=2048)

    # 
    string2 = models.TextField(max_length=2048)

    # 地址
    flag1 = models.CharField(max_length=200)

    # 
    flag2 = models.CharField(max_length=200)

    # string1 varchar(1024), string2 varchar(1024),flag1 varchar(128),flag2 varchar(128)