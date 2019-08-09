from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class P4node(models.Model):
    product_id = models.CharField(max_length=50)
    username = models.CharField(max_length=20,blank=True, null=True)
    status1 = models.CharField(max_length=7,default='off')
    status2 = models.CharField(max_length=7,default='off')
    status3 = models.CharField(max_length=7,default='off')
    status4 = models.CharField(max_length=7,default='off')

    def __str__(self):
        return '4Node : ' + str(self.product_id)


class P8node(models.Model):
    product_id = models.CharField(max_length=50)
    username = models.CharField(max_length=20,blank=True, null=True)
    status1 = models.CharField(max_length=7,default='off')
    status2 = models.CharField(max_length=7,default='off')
    status3 = models.CharField(max_length=7,default='off')
    status4 = models.CharField(max_length=7,default='off')
    status5 = models.CharField(max_length=7,default='off')
    status6 = models.CharField(max_length=7,default='off')
    status7 = models.CharField(max_length=7,default='off')
    status8 = models.CharField(max_length=7,default='off')

    def __str__(self):
        return '8Node : ' + str(self.product_id)


class Extendeduser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    product_id = models.CharField(max_length=50, blank=True, null=True)
    product_type = models.CharField(max_length=20, blank=True, null=True)
    phone_num = models.IntegerField()

    def __str__(self):
        return str(self.user) + " : " + str(self.product_id)
