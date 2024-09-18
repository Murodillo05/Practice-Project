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
    is_active = models.BooleanField(default=True)

    def str(self):
        return self.name