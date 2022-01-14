from django.db import models

from shared.django.model import BaseModel


class Client(BaseModel):
    user = models.OneToOneField('users.User', models.CASCADE, related_name='clients')

    def __str__(self):
        return self.user.username
