from django.db import models


class Discounts(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    back_image = models.ImageField(upload_to="Image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Program_info(models.Model):
    program_name = models.CharField(max_length=20)
    text = models.CharField(max_length=60)
    is_active = models.BooleanField(default=True)
    
class Program(models.Model):
    image = models.ImageField(upload_to='images/')
    bank_name = models.CharField(max_length=20)
    program = models.CharField(max_length=30)
    betting = models.CharField(max_length=10)
    perviy_vznos = models.CharField(max_length=10)
    year_deadline = models.CharField(max_length=10)
    monthly_cost = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __init__(self):
        return self.program


class Questions(models.Model):
    name = models.CharField(max_length=16)
    phone_number = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __init__(self):
        return self.name
    

class Testimonal(models.Model):
    image = models.ImageField(upload_to='images/')
    full_name = models.CharField(max_length=30)
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    def __init__(self):
        return self.full_name


class About(models.Model):
    text = models.TextField()
    image = models.ImageField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text
    

class Service(models.Model):
    image = models.ImageField(upload_to='')
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
