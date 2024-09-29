from django.db import models

# Create your models here.
class Type(models.Model):
    name=models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.name


class Item(models.Model):
    name= models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    number = models.IntegerField()
    lastDate = models.DateField()
    def __str__(self):
        return self.name
