from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.
class CAR(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    car_model = models.CharField(max_length=100)
    color = models.CharField(max_length=30)
    image = models.ImageField(upload_to='car_images/')  
    phone_number=models.CharField(max_length=20,null=True,# Adjust based on your needs
        validators=[
            RegexValidator(
                regex=r'^\+?91?\d{10,15}$',  # Example regex for international phone numbers
                message="Phone number must be entered in the format: '+91 999999999'. Up to 10 digits allowed.")])

    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.TextField(null=True)

    def __str__(self):
        return self.car_model