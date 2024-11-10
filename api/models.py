from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Dept(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now=True)