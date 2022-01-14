from django.db import models

from shared.django.model import BaseModel


class Car(BaseModel):
    number = models.CharField(max_length=8)
    model = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    seria_number = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.number


class Driver(BaseModel):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='drivers')
    car = models.ForeignKey('drivers.Car', on_delete=models.PROTECT, related_name='drivers')

    balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username
