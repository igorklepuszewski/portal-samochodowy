from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
# Create your models here.

class CarMain(models.Model):
    make = models.CharField(max_length=16)
    model = models.CharField(max_length=32)

class CarDetail(models.Model):
    CAR_COLORS = [
        ("RED", "Red"),
        ("BLU", "Blue"),
        ("YEL", "Yellow"),
        ("BLA", "Black"),
        ("WHI", "White")
    ]
    CAR_FUELS = [
        ("DIE", "Diesel"),
        ("PET", "Petrol"),
        ("HYB", "Hybrid"),
        ("LPG", "LPG"),
        ("ELE", "Electric"),
    ]
    production_date = models.DateField()
    color = models.CharField(max_length=3, choices=CAR_COLORS, default="BLA")
    seats = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    fuel = models.CharField(max_length=3, choices=CAR_FUELS, default="PET")
    power = models.PositiveIntegerField()

class Car(models.Model):
    main = models.ForeignKey(CarMain, on_delete=models.CASCADE)
    detail = models.OneToOneField(CarDetail, on_delete=models.PROTECT)

    def delete(self):
        super(Car, self).delete()
        self.detail.delete()

    def __str__(self):
        return f"{self.main.make} {self.main.model}"

