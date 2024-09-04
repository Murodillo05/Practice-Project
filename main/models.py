from django.db import models

# Create your models here.
class Discounts(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    
    back_image = models.ImageField(upload_to="Image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name
    


class About(models.Model):
    text = models.TextField()
    image = models.ImageField()

    def __str__(self) -> str:
        return self.text
    

class Service(models.Model):
    image = models.ImageField(upload_to='')
    description = models.CharField(max_length=255)