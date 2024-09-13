from django.db import models


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
    

class Program_info(models.Model):
    program_name = models.CharField(max_length=20)
    text = models.CharField(max_length=60)
    
class Program(models.Model):
    image = models.ImageField(upload_to='images/')
    bank_name = models.CharField(max_length=20)
    program = models.CharField(max_length=30)
    betting = models.CharField(max_length=10)
    perviy_vznos = models.CharField(max_length=10)
    year_deadline = models.CharField(max_length=10)
    monthly_cost = models.CharField(max_length=50)


    def __init__(self):
        return self.program


class Questions(models.Model):
    name = models.CharField(max_length=16)
    phone_number = models.IntegerField()

    def __init__(self):
        return self.name
    

class Testimonal(models.Model):
    image = models.ImageField(upload_to='images/')
    full_name = models.CharField(max_length=30)
    text = models.TextField()
#rfjrgh
    def __init__(self):
        return self.full_name


class About(models.Model):
    text = models.TextField()
    image = models.ImageField()

    def __str__(self) -> str:
        return self.text
    

class Service(models.Model):
    image = models.ImageField(upload_to='')
    description = models.CharField(max_length=255)



class Apartments(models.Model):
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)
    number_of_apartments = models.CharField(max_length=255)
    standard_price = models.CharField(max_length=90)
    credit = models.CharField(max_length=90)
    credit_time = models.CharField(max_length=70)
    apartmentsand_studios = models.CharField(max_length=90)
    price = models.CharField(max_length=255)
    fields = models.CharField(max_length=40)
    location = models.CharField(max_length=255)


    def __str__(self):
        return self.name
    

class Apartments_info(models.Model):
    rooms_of_apartment_and_metres = models.CharField(max_length=255)
    standard_price = models.CharField(max_length=255)
    recomendations = models.CharField(max_length=255)
    metres = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    korpus = models.CharField(max_length=30)
    ochered = models.CharField(max_length=40)
    sdacha = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.rooms_of_apartment_and_metres
    