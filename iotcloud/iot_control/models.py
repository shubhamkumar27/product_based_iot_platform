from django.db import models

# Create your models here.
class Buttons(models.Model):
    number = models.IntegerField()
    status = models.CharField(max_length=7,default='off')

    def __str__(self):
        return str(self.number) + ' : ' + str(self.status)
